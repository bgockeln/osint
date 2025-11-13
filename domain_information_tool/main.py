
import sys
import whois
import os
import socket
import requests
import json
import time
# Helper Functions
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def wait():
    input("Press any key")

def exit_script():
    print("Exiting...")
    sys.exit(0)

# Lookup functions
def whois_lookup():
    domain = input("Please enter a domain (e.g. www.example.com): ").strip()
    domain = domain.replace("https://", "").replace("http://", "").split("/")[0]
   
    try:
        info = whois.whois(domain)
        print("\nWHOIS Information:")
        print(f"Domain: {info.domain_name}")
        print(f"Registrar: {info.registrar}")
        print(f"Creation Date: {info.creation_date}")
        print(f"Expiration Date: {info.expiration_date}")
        print(f"Name Servers: {info.name_servers}")
        print(f"Emails: {info.emails}")
    except Exception as e:
        print(f"Error retrieving WHOIS data: {e}")

    wait()

def dns_lookup():
    domain = input("Please enter a domain (e.g. www.example.com): ").strip()
    domain = domain.replace("https://", "").replace("http://", "").split("/")[0]
    
    try:
        # gethostbyname_ex returns (hostname, aliaslist, ipaddrlist)
        host_info = socket.gethostbyname_ex(domain)
        hostname, aliases, ip_list = host_info

        print(f"\nDNS Information for {domain}:")
        print(f"Hostname: {hostname}")
        print(f"Aliases: {', '.join(aliases) if aliases else 'None'}")
        print(f"IP Addresses: {','.join(ip_list)}")

    except socket.gaierror:
        print(f"Could not resolve domain: {domain}")
    except Exception as e:
        print(f"Error during DNS lookup: {e}")

    wait()

def geoloc_lookup():
    domain = input("Please enter a domain (e.g. www.example.com): ").strip()
    domain = domain.replace("https://", "").replace("http://", "").split("/")[0]

    try:
        # Resolve domain to IP
        ip = socket.gethostbyname(domain)

        # Query IP geolocation API
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,isp,org,as,query")
        data = response.json()

        if data["status"] == "success":
            print(f"\nGeolocation Information for {domain} ({ip}):")
            print(f"Country: {data.get('country')}")
            print(f"Region: {data.get('regionName')}")
            print(f"City: {data.get('city')}")
            print(f"ISP: {data.get('isp')}")
            print(f"Organization: {data.get('org')}")
            print(f"ASN: {data.get('as')}")
        else:
            print(f"Error: {data.get('message')}")
    except socket.gaierror:
        print(f"Could not resolve domain: {domain}")
    except requests.RequestException as e:
        print(f"Error contacting geolocation API: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    wait()

def fingerprint_lookup():
    domain = input("Please enter a domain (e.g. www.example.com): ").strip()
    domain = domain.replace("https://", "").replace("http://", "").split("/")[0]
    
    # Try both http and https
    urls = [f"http://{domain}", f"https://{domain}"]
    success = False

    for url in urls:
        try:
            response = requests.head(url, timeout=5)
            if response.status_code < 400:
                headers = response.headers
                print(f"\nWeb Server Fingerprint for {url}")
                print(f"Server: {headers.get('Server', 'Unknown')}")
                print(f"X-Powered-By: {headers.get('X-Powered-By', 'Unknown')}")
                print(f"Content-Type: {headers.get('Content-Type', 'Unknown')}")
                print(f"Other headers: ")
                for key, value in headers.items():
                    if key not in ['Server', 'X-Powered-By', 'Content-Type']:
                        print(f"    {key}: {value}")
                success = True
                break # Stop after first successful request
        except requests.RequestException:
            continue

    if not success:
        print(f"Could not retrieve headers for {domain}")
        
    wait()

def shodan_lookup():
    """
    Resolve a domain to IP, query Shodan's Host API for that IP and print a concise report.
    Requires SHODAN_API_KEY environment variable, or the user can paste a key when prompted.
    """
    domain = input("Please enter a domain (e.g. www.example.com): ").strip()
    domain = domain.replace("https://", "").replace("http://", "").split("/")[0]

    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        print(f"Could not resolve domain: {domain}")
        wait()
        return
    
    # Get API key from env or ask user
    api_key = os.environ.get("SHODAN_API_KEY")
    if not api_key:
        print("No SHODAN_API_KEY environment variable found")
        api_key = input("Enter Shodan API key (or press Enter to cancel): ").strip()
        if not api_key:
            print("Skipping Shodan lookup (no API key).")
            wait()
            return
    
    url = f"https://api.shodan.io/shodan/host/{ip}"
    params = {"key": api_key}

    try:
        resp = requests.get(url, params=params, timeout=10)
        if resp.status_code == 401:
            print("Authentication failed: invalid Shodan API key.")
            wait()
            return
        if resp.status_code == 404:
            print(f"No results on Shodan for {ip} ({domain}).")
            wait()
            return
        elif resp.status_code != 200:
            # For example 403, still try to parse JSON
            try:
                data = resp.json()
            except Exception:
                print(f" Shodan returned {resp.status_code}, could not parse JSON")
                wait()
                return
        else:
            data = resp.json()

        # Print a summary
        print(f"\nShodan Host Report for {domain} ({ip}):")
        print(f"Hostnames: {', '.join(data.get('hostnames', [])) or 'None'}")
        print(f"Organization: {data.get('org', 'Unknown')}")
        print(f"ISP: {data.get('isp', 'Unknown')}")
        print(f"Operating System: {data.get('os', 'Unknown')}")
        print(f"Last update: {data.get('last_update', 'Unknown')}")
        print(f"Open ports: {', '.join(str(p) for p in data.get('ports', [])) or 'None'}")

        # Show banners (service/product info)
        banners = data.get('data', [])
        if banners:
            print("\nTop service banners (first 6):")
            for entry in banners[:6]:
                port = entry.get('port')
                banner = entry.get('data', '').strip().splitlines()[0]
                product = entry.get('product') or entry.get('http', {}).get('title') or None
                print(f" - Port {port}: {product or banner[:150]}")

        # Vulnerabilities (CVE if present)
        vulns = data.get('vulns') or {}
        if vulns:
            print("\nVulnerabilities found (CVE list):")
            for cve in vulns:
                print(f" - {cve}")
        else:
            print("\nVulnerabilities_ None listed by Shodan")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error from Shodan: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Network error while contacting Shodan: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    
    wait()

# Main loop    
def main():
    menu_actions = {
        "1": whois_lookup,
        "2": dns_lookup,
        "3": geoloc_lookup,
        "4": fingerprint_lookup,
        "5": shodan_lookup,
        "6": exit_script
    }

    while True:
        clear_screen()
        print("\nBen's Domain Information Lookup Tool")
        print("1. WHOIS lookup")
        print("2. DNS resolution")
        print("3. IP geolocation")
        print("4. Web server fingerprint")
        print("5. Shodan lookup(Experimental)")
        print("6. Exit")
        choice = input("Enter choice: ").strip()
        action = menu_actions.get(choice)

        if action:
            action()
        else:
            print("Invalid Choice, try again.")
            wait()
            clear_screen()

if __name__ == "__main__":
    main()