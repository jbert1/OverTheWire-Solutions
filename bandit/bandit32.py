import paramiko
import paramiko.client
from sys import argv
from time import sleep

next_level = argv[0].split('/')[-1].split('\\')[-1][:-3]

username = f"bandit{int(next_level[6:]) - 1}"

with open(f"./passwords/{username}.pass", 'r') as f:
    password = f.read()

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname="bandit.labs.overthewire.org",
    port=2220,
    username=username,
    password=password
)

shell = client.invoke_shell()
shell.settimeout(5.0)

sleep(0.2)
shell.send(b'cd $(mktemp -d)\n')
sleep(0.2)
shell.send(b'git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo\n')
sleep(1.0)
shell.send(b'yes\n')
sleep(1.0)
shell.send(password.encode() + b'\n')
sleep(1.0)
shell.send(b'cd ./repo\n')
sleep(0.2)
shell.send(b'rm ./.gitignore && echo "May I come in?" > key.txt && git add -A && git commit -m "key.txt" && git push\n')
sleep(0.2)
shell.send(b'yes\n')
sleep(1.0)
shell.send(password.encode() + b'\n')
sleep(1.0)
new_password = shell.recv(8192).split(b'\r\nremote: ')[-4][:-4].decode()

print(new_password)

shell.close()
client.close()

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
