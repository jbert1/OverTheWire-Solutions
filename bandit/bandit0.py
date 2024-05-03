import paramiko
import paramiko.client

username = "bandit0"

with open(f"./passwords/{username}.pass") as f:
    password = f.read()

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname="bandit.labs.overthewire.org",
    port=2220,
    username=username,
    password=password
)


_stdin, _stdout, _stderr = client.exec_command('whoami')

print(_stdout.read().decode())

client.close()
