# level_up

## network automation day 1

- **Step 1**
```
curl -s https://raw.githubusercontent.com/greaselovely/level_up/main/network_automation_day_1/install_python312.sh | bash
```

- **Step 2**
Create a new file called `hello_world.py` using notepad or any other text editor.
Type the following into this new file:
```
print("Hello World!")
```

Execute the file:
```
python3 hello_world.py
```

- **Step 3**
Create a new file called `indent.py` using notepad or any other text editor.
Type the following into this new file:
```

```


- **Step 4**
Create a new file called `get_ip.py` using notepad or any other text editor.
Type the following into this new file:
```
import requests

url = "https://ipecho.net/plain"

ip = requests.get(url)

print(f"My IP is {ip.text}")
```

Execute the file:
```
python3 get_ip.py
```