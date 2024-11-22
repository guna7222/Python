import requests
import config

url = config.get_users() + '7537329'

headers = dict()
headers['Authorization'] = config.get_bearer_token()

response = requests.delete(url, headers=headers)

if response.status_code != 204 or response.status_code !=404:
    print("resource not deleted")
else:
    print("resource deleted")
