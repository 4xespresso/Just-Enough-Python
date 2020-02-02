import telnetlib
import time

username = "python-user"
password = "InsightInsight"
individual_host = "10.128.0.26"
telnet_port = 23
timeout = 5 #seconds

# Here we create a Telnet object using the telnetlib library. This
# object uses the previously assigned values for port and timeout. Once
# created, it connects to the remote host and we can read data from the
# connection, taking action after a certain period of time or after
# seeing particular output.

# Open telnet session using telnetlib object to previously specified host
telnet = telnetlib.Telnet(individual_host, telnet_port, timeout)

# Wait for username prompt and then log in.
telnet.read_until(b"sername:", 3)
time.sleep(2)
telnet.write(username.encode('ascii') + b"\n")
time.sleep(2)

# Wait for password prompt and then log in.
telnet.read_until(b"assword:", 3)
telnet.write(password.encode('ascii') + b"\n")
time.sleep(2)

# Now we send commands to the remote host. Note the difference in the
# structure of the command compared to Paramiko.
telnet.write(b"terminal length 0\n")
time.sleep(2)
telnet.write(b"show interface\n")
time.sleep(2)
telnet.write(b"logout\n")
time.sleep(2)

# Decode the output from binary to ascii from the remote host and then print.
telnet_output = (telnet.read_very_eager().decode('ascii'))
print("--- Begin telnetlib output for " + individual_host + " ---")
print(telnet_output)
print("--- End telnetlib output for " + individual_host + " ---")