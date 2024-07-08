import requests

url = "https://ipecho.net/plain"

ip = requests.get(url)

print(f"My IP is {ip.text}")