import telnetlib
import time

username = "python-user"
password = "InsightInsight"
individual_host = "10.128.0.26"

telnet = telnetlib.Telnet(individual_host, 23, 5)
telnet.read_until(b"sername:", 3)
time.sleep(2)
telnet.write(username.encode('ascii') + b"\n")
time.sleep(2)
telnet.read_until(b"assword:", 3)
telnet.write(password.encode('ascii') + b"\n")
time.sleep(2)
telnet.write(b"terminal length 0\n")
time.sleep(2)
telnet.write(b"show interface\n")
time.sleep(2)
telnet.write(b"logout\n")
time.sleep(2)
telnet_output = (telnet.read_very_eager().decode('ascii'))
print(telnet_output)
