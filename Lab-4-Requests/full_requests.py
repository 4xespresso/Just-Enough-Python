import requests
from requests.auth import HTTPBasicAuth

username = "python-user"
password = "InsightInsight"
individual_host = "10.128.0.26"

# Here in this block, we are using the Python requests module to query
# the REST API of a Cisco router for interface information.'''

# Create the url for the request using the host which the script is
# currently working on. Then send the HTTP request to the remote host.

url_request = "http://" + individual_host + "/level/15/exec/-/show/interface/CR"
response = requests.get(url_request, auth=HTTPBasicAuth(username, password))

# Convert raw HTML to ASCII character set and print
print("--- Begin HTTP requests output for " + individual_host + " ---")
print(response.content.decode('ascii'))
print("--- End HTTP requests output for " + individual_host + " ---")