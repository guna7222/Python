import requests

url = 'https://gorest.co.in/public/v2/users'
user_details = requests.get(url)

# text format
print(user_details.text)

# json() format
print(user_details.json())

# status_code
print(user_details.status_code)

# url
print(user_details.url)

# content - gets binary format
print(user_details.content)
