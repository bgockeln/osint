import requests

username = input("Enter a username to check: ")
print(f"Checking public profiles for: {username}")

# Urls to query
url = f"https://github.com/{username}"

# Check for username
response = requests.get(url)

# Check result
if response.status_code == 200:
    print(f"Found Github profile: {url}")
elif response.status_code == 404:
    print(" No Github profile found.")
else:
    print(f" Got unexpected status code: {response.status_code}")
