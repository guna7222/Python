import requests

url = 'https://gorest.co.in/public/v2/users/7533023'

name = input("Enter name")
data = dict()
data['name'] = name

ACCESS_TOKEN = '194132ac555291af78c6b6060e5e0c11b729a7b9bd72c0da3acbc06c302220d3' 
headers = dict()
headers['Authorization'] = 'Bearer ' + ACCESS_TOKEN
print(headers)
response = requests.put(url, data = data, headers = headers)
print(response.status_code)
print(response.json())
