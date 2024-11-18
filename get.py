import requests

# getting all users details from the users end point 
x = requests.get('https://gorest.co.in/public/v2/users')
print(x.json())
