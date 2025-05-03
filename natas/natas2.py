from requests import get
from sys import argv

next_level = argv[0].split('/')[-1].split('\\')[-1][:-3]

username = f"natas{int(next_level[5:]) - 1}"

URL = f"http://{username.split('.')[0]}.natas.labs.overthewire.org"

with open(f"./passwords/{username}.pass", 'r') as f:
    password = f.read()

resp = get(URL, auth=(username, password))

lines = resp.text.split('\n')

# Password in comments
for line in lines:
    if "The password for natas2 is" in line:
        new_password = line.split(' ')[5]
        break

print(new_password)

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
