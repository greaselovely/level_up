# level_up

## network automation day 1

- **Step 1**
`curl -s https://raw.githubusercontent.com/greaselovely/level_up/main/network_automation_day_1/install_python312.sh | bash`

- **Step 2**
Create a new file called `get_ip.py` using notepad or any other text editor.
Type the following into this new file:
```
import requests

url = "https://ipecho.net/plain"

ip = requests.get(url)

print(f"My IP is {ip.text}")
```