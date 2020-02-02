from netmiko import Netmiko

username = "python-user"
password = "InsightInsight"
individual_host = "10.128.0.26"

# Here we create a Netmiko object. The Netmiko library is expecting a
# list of keyword arguments, like this:
net_connect = Netmiko(
    host=individual_host,
    username=username,
    password=password,
    device_type='cisco_ios')

# Use Netmiko to send the command to the device. Capture the output of
# the command in the variable "output".
netmiko_command = "show ip int brief"
netmiko_output = net_connect.send_command(netmiko_command)

# Close the connection.
net_connect.disconnect()

# Display the response send back from the device in the Python console.
print("--- Begin Netmiko output for " + individual_host + " ---")
print(netmiko_output)
print("--- End Netmiko output for " + individual_host + " ---")
