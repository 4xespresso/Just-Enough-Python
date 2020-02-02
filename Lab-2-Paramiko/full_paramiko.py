import paramiko
import time

username = "python-user"
password = "InsightInsight"
individual_host = "10.128.0.26"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=individual_host, username=username, password=password, timeout=5)
remote_connection = ssh_client.invoke_shell()
remote_connection.send("terminal length 0\n")
time.sleep(2)
remote_connection.send("show interface\n")
time.sleep(2)
remote_connection.send("logout\n")
time.sleep(2)
ssh_output = remote_connection.recv(128000).decode('utf-8')
print(ssh_output)
ssh_client.close
