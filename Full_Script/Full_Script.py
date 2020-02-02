import telnetlib
import paramiko
import time
import requests
from requests.auth import HTTPBasicAuth
from netmiko import Netmiko

#Prepare some variables that we will re-use later. Having them in one place
#here makes it easy to  change what we are doing in the code without digging
#through the code and changing it in multiple places.
host_list= ["10.128.0.26", "10.128.0.27", "10.128.0.28"]
username = "python-user"
password = "InsightInsight"
timeout = 5 #seconds
telnet_port = 23

# Do this whole series of steps for each host in the list we defined above.
for individual_host in host_list:
    try:
        '''Here we create a Netmiko object. The Netmiko library is expecting a	 	 
        list of keyword arguments, like this:'''
        net_connect = Netmiko(
             host = individual_host,
             username = username,
             password = password,
             device_type = 'cisco_ios')


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

    # The 'except' block runs if there is any sort of error encountered in
    # the 'try' block. It's a great way of handling code execution when
    # you want to account for possible exceptions (errors).'''
    # print('Exception occurred during Netmiko block.')
    except:
        print("Exception occurred during Netmiko block.")

    try:
        ''' Here we create an object representing a connection using the Paramiko	 	 
        library's SSHClient.'''
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
    except:
        print("Exception occurred during Paramiko block.")


    try:
        ''' Here we create a Telnet object using the telnetlib library. This	 	 
        object uses the previously assigned values for port and timeout. Once	 	 
        created, it connects to the remote host and we can read data from the	 	 
        connection, taking action after a certain period of time or after	 	 
        seeing particular output.'''

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
    except:
        print("Exception occurred during the telnetlib block")

    try:
        '''Here in this block, we are using the Python requests module to query 
        the REST API of a Cisco router for interface information.'''

        # Create the url for the request using the host which the script is
        # currently working on. Then send the HTTP request to the remote host.
        url_request = "http://" + individual_host + "/level/15/exec/-/show/interface/CR"
        response = requests.get(url_request, auth=HTTPBasicAuth(username, password))

        # Convert raw HTML to ASCII character set and print
        print("--- Begin HTTP requests output for " + individual_host + " ---")
        print(response.content.decode('ascii'))
        print("--- End HTTP requests output for " + individual_host + " ---")
    except:
        print("Exception occurred during the HTTP API Block")
