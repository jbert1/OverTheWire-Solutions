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

_stdin, _stdout, _stderr = client.exec_command('cat README.txt')

end_text = _stdout.read().decode()

print(end_text)

client.close()

with open(f"./passwords/{next_level}.end", 'w') as f:
    f.write(end_text)
