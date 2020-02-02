from netmiko import Netmiko

username = "python-user"
password = "InsightInsight"
individual_host = "10.128.0.26"

cisco1 = {"host": individual_host, "username": username, "password": password, "device_type": "cisco_ios"}
netmiko_command = "show ip int brief"
net_connect = Netmiko(**cisco1)
output = net_connect.send_command(netmiko_command)
net_connect.disconnect()
print(output)
