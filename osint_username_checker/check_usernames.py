import requests
import sys
import os
import time

# Helper Functions
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def wait():
    input("Press any key")

def exit_script():
    print("Exiting...")
    sys.exit(0)

# Github
def github():
    username = input("Enter a username to check: ")
    print(f"Checking public profiles for: {username}")
    url = f"https://github.com/{username}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}
    # Check for username
    response = requests.get(url, headers=headers)

    # Check result
    if response.status_code == 200:
        print(f"Found Github profile: {url}")
    elif response.status_code == 404:
        print(" No Github profile found.")
    else:
        print(f" Got unexpected status code: {response.status_code}")

    time.sleep(1)  # pause 1 second before asking for input
    wait()

# Instagram
def instagram():
    username = input("Enter a username to check: ")
    print(f"Checking public profiles for: {username}")
    url = f"https://instagram.com/{username}/"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}
    # Check for username
    response = requests.get(url, headers=headers)

    # Check result
    body = response.text.lower()
    if response.status_code == 404 or \
       "sorry, this page isn't available" in body or \
       "the link you followed may be broken" in body:
        print("No Instagram profile found.")
    elif response.status_code == 200:
        print(f"Found Instagram profile: {url}")
    else:
        print(f"Got unexpected status code: {response.status_code}")
    
    time.sleep(1)  # pause 1 second before asking for input
    wait()

# Tiktok
def tiktok():
    username = input("Enter a username to check: ")
    print(f"Checking public profiles for: {username}")
    url = f"https://tiktok.com/@{username}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}
    # Check for username
    response = requests.get(url, headers=headers)

    # Check result
    body = response.text.lower()
    if response.status_code == 404 or "page not found" in body or "couldn't find this account" in body:
        print("No TikTok profile found.")
    elif response.status_code == 200:
        print(f"Found TikTok profile: {url}")
    else:
        print(f"Got unexpected status code: {response.status_code}")
    
    time.sleep(1)  # pause 1 second before asking for input
    wait()

# X/Twitter
def x():
    username = input("Enter a username to check: ")
    print(f"Checking public profiles for: {username}")
    url = f"https://x.com/{username}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}
    # Check for username
    response = requests.get(url, headers=headers)

    # Check result
    body = response.text.lower()
    if response.status_code == 404 or "account suspended" in body or "does not exist" in body:
        print("No X (Twitter) profile found.")
    elif response.status_code == 200:
        print(f"Found X (Twitter) profile: {url}")
    else:
        print(f"Got unexpected status code: {response.status_code}")
    
    time.sleep(1)  # pause 1 second before asking for input
    wait()

# Main loop
def main():
    menu_actions = {
            "1": github,
            "2": instagram,
            "3": tiktok,
            "4": x,
            "5": exit_script
    }

    while True:
        clear_screen()
        print("\nBen's Username Checker")
        print("1. Github")
        print("2. Instagram")
        print("3. Tiktok")
        print("4. X/Twitter")
        print("5. Exit")
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