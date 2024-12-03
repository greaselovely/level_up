import requests
from getpass import getpass
import base64
import urllib3
import xmltodict
import re
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Placeholder for API command - students should paste the command here
api_command = "/api/?type=op&cmd=<show><system><info></info></system></show>"

# Base64-encoded version of the correct API command for validation - just used in class only
expected_api_command_hash = "L2FwaS8/dHlwZT1vcCZjbWQ9PHNob3c+PHN5c3RlbT48aW5mbz48L2luZm8+PC9zeXN0ZW0+PC9zaG93Pg=="

def is_valid_ipv4(ip):
    """Validate an IPv4 address."""
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return bool(pattern.match(ip)) and all(0 <= int(octet) <= 255 for octet in ip.split("."))

def get_firewall_ips():
    """Retrieve firewall IPs from file or prompt the user for input."""
    if os.path.exists("firewalls.txt"):
        with open("firewalls.txt", "r") as file:
            ips = [line.strip() for line in file.readlines()]
        print("Loaded IPs from firewalls.txt")
    else:
        ips = []
        print("firewalls.txt not found. Please enter IPs. Press Enter on a blank line to finish.")
        while True:
            ip = input("Enter firewall IP: ")
            if ip == "":
                break
            if is_valid_ipv4(ip):
                ips.append(ip)
            else:
                print(f"{ip} is not a valid IPv4 address and will be discarded.")
        
        with open("firewalls.txt", "w") as file:
            file.write("\n".join(ips))
        print("IP addresses saved to firewalls.txt")
    
    return ips

def get_user_input():
    """Prompt user for username and password."""
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    return username, password

def authenticate_to_firewall(firewall_ip, username, password):
    """Authenticate against the NGFW and retrieve an API key."""
    url = f"https://{firewall_ip}/api/?type=keygen&user={username}&password={password}"
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        api_key = response.text.split("<key>")[1].split("</key>")[0]
        print(f"Successfully authenticated to {firewall_ip} and retrieved API key.")
        return api_key
    except Exception as e:
        print(f"Failed to authenticate: {e}")
        return None

def check_api_command():
    """Ensure the API command variable is set and matches the expected value."""
    if not api_command:
        print("API command not entered. Please set the 'api_command' variable in the script.")
        return False
    
    api_command_hash = base64.b64encode(api_command.encode()).decode()
    if api_command_hash != expected_api_command_hash:
        print("The API command is incorrect. Please verify your entry.")
        return False
    
    return True

def execute_command(firewall_ip, api_key):
    """Execute the API command to retrieve system information."""
    url = f"https://{firewall_ip}{api_command}&key={api_key}"
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        print(f"System Information Retrieved from {firewall_ip}")
        return response.text
    except Exception as e:
        print(f"Failed to retrieve system information: {e}")
        return None

def display_system_info(xml_data):
    """Parse and print the hostname, serial number, and PAN-OS version in a tab-delimited format."""
    try:
        parsed_data = xmltodict.parse(xml_data)
        system_info = parsed_data['response']['result']['system']
        hostname = system_info['hostname']
        serial_number = system_info['serial']
        panos_version = system_info['sw-version']
        
        print(f"{hostname}\t{serial_number}\t{panos_version}")
    except KeyError as e:
        print(f"Error parsing system info: {e}")

def main():
    """Main function to run the script."""
    if not check_api_command():
        return

    firewall_ips = get_firewall_ips()
    username, password = get_user_input()

    for firewall_ip in firewall_ips:
        api_key = authenticate_to_firewall(firewall_ip, username, password)
        xml_data = execute_command(firewall_ip, api_key)
        
        # Directly call display_system_info without conditional nesting
        display_system_info(xml_data)

if __name__ == "__main__":
    main()
