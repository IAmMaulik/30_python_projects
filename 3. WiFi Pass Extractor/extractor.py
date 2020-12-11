import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

wifis = [line.split(":")[1][1:-1] for line in data if 'All User Profile' in line]

for wifi in wifis:
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key', '=', 'clear']).decode('utf-8').split('\n')
    result = [line.split(':')[1][1:-1] for line in result if 'Key Content' in line]
    try:
        print(f'Name: {wifi}, Password: {result[0]}')
    except:
        print(f'Name: {wifi}, Password: Not Availible')

print(wifis)