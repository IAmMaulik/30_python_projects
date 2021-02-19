import socket
from requests import get

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get("https://api.ipify.org").text

print(f"Hostname: {hostname}")
print(f"Local IP Address: {local_ip}")
print(f"Public IP Address: {public_ip}")
