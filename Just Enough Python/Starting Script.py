import telnetlib
import paramiko
import time
import requests
from netmiko import Netmiko

host_list= ["10.128.0.26", "10.128.0.27", "10.128.0.28"]
username = 'chad'
password = 'p@ssw@rd'


for individual_host in host_list:
    try:
        cisco1 = {"host": individual_host, "username": username, "password": password, "device_type": "cisco_ios"}
        netmiko_command = "show ip int brief"
        net_connect = Netmiko(**cisco1)
        output = net_connect.send_command(netmiko_command)
        net_connect.disconnect()
        print(output)
    except:
        print("Do Nothing")

    try:
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
    except:
        print("Do nothing")


    try:
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
    except:
        print("Do nothing")

    try:
        httpHeaders = {"Authorization": "Basic Y2hhZDpwQHNzd0ByZA=="}
        url_request = ("http://" + individual_host + "/level/15/exec/-/show/ip/interface/CR")
        response = requests.get(url_request, headers=httpHeaders)
        print(response.content)
    except:
        print("Do nothing")
