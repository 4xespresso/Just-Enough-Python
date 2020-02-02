import requests
from requests.auth import HTTPBasicAuth

username = "python-user"
password = "InsightInsight"
individual_host = "10.128.0.26"

url_request = ("http://" + individual_host + "/level/15/exec/-/show/ip/interface/CR")
response = requests.get(url_request, auth=HTTPBasicAuth(username, password))
print(response.content)