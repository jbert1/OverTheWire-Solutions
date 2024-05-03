import paramiko
import paramiko.client

username = "bandit1"

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


_stdin, _stdout, _stderr = client.exec_command('cat ~/-')

new_password = _stdout.read().decode().replace('\n', '')

print(new_password)

client.close()

with open(f"./passwords/bandit{int(username[6:]) + 1}.pass", 'w') as f:
    f.write(new_password)
