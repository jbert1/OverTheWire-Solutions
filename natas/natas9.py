from requests import get, post
from sys import argv

from binascii import unhexlify
from base64 import b64decode

# Captured from index-source.html
encoded_secret = "3d3d516343746d4d6d6c315669563362"

secret = b64decode(unhexlify(encoded_secret.encode())[::-1]).decode()

next_level = argv[0].split('/')[-1].split('\\')[-1][:-3]

username = f"natas{int(next_level[5:]) - 1}"

URL = f"http://{username.split('.')[0]}.natas.labs.overthewire.org"

with open(f"./passwords/{username}.pass", 'r') as f:
    password = f.read()

resp = post(URL, data={'secret': secret, 'submit': "Submit+Query"}, auth=(username, password))

lines = resp.text.split('\n')

# Password in page
for line in lines:
    if "natas9" in line:
        new_password = line.split(' ')[7]
        break

print(new_password)

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
