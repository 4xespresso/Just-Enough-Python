import paramiko
import time

username = "python-user"
password = "InsightInsight"
individual_host = "10.128.0.26"
timeout = 5 #seconds

# Here we create an object representing a connection using the Paramiko
# library's SSHClient.
ssh_client = paramiko.SSHClient()

# If the local computer does not have a host key for the remote host we
# are connecting to, automatically add it.
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Now we tell the connection object to connect. We re-use the variables
# we created at the beginning of the file.
ssh_client.connect(hostname=individual_host, username=username, password=password, timeout=timeout)
remote_connection = ssh_client.invoke_shell()
remote_connection.send("terminal length 0\n")
time.sleep(2)
remote_connection.send("show interface\n")
time.sleep(2)
remote_connection.send("logout\n")
time.sleep(2)

# Here we take the data from the SSH connection's receive buffer
# and decode it using UTF-8. (8-bit Unicode Transformation Format). Then
# we print it out, and close the connection.'''
ssh_output = remote_connection.recv(128000).decode('utf-8')
print("--- Begin Paramiko output for " + individual_host + " ---")
print(ssh_output)
print("--- End Paramiko output for " + individual_host + " ---")

# Now we'll close the SSH session.
ssh_client.close()
