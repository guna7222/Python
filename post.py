import requests

url = 'https://gorest.co.in/public/v2/users'



name = input("enter your name : ")
email = input("enter your email : ")
gender = input("enter gender : ")
status = input("enter status : ")

data = dict()
data['name'] = name
data['email'] = email
data['gender'] = gender
data['status'] = status

print(data)

# this is not a best practice instead store access token in then env variable
# export ACCESS_TOKEN = '194132ac555291af78c6b6060e5e0c11b729a7b9bd72c0da3acbc06c302220d3'
# import os
# os.getenv('ACCESS_TOKEN')

ACCESS_TOKEN = '194132ac555291af78c6b6060e5e0c11b729a7b9bd72c0da3acbc06c302220d3' 

headers = dict()
headers['Authorization'] = 'Bearer ' + ACCESS_TOKEN
print(headers)


post1 = requests.post(url, data=data, headers=headers)
print(post1)
