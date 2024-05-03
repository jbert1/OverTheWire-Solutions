import paramiko
import paramiko.client
from sys import argv

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

sftp = client.open_sftp()
sftp.get("sshkey.private", "./passwords/bandit14.key")

sftp.close()
client.close()

client.connect(
    hostname="bandit.labs.overthewire.org",
    port=2220,
    username=next_level,
    key_filename=f"./passwords/{next_level}.key"
)

_stdin, _stdout, _stderr = client.exec_command('cat /etc/bandit_pass/bandit14')

new_password = _stdout.read().decode().replace('\n', '')

print(new_password)

client.close()

with open(f"./passwords/{next_level}.pass", 'w') as f:
    f.write(new_password)
