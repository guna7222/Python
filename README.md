# Python
## Requests Module
import requests 
- requests module allows you to send http request via Python.
- we can make different Rest Api calls by using requests moudle/libraray
## config.py
#Best Practices
 - BASE_URL = ' '
 - BASE_PATH = ' '
 - VERSION = ' '
 - USERS = ' '
## Helper Function

- def users():
    return BASE_URL + BASE_PATH + VERSION + USERS

## get.py
import requests
import config

user_details = requests.get(config.users())
printf(user_details.json())

# general way
import requests

x = requests.get('https://gorest.co.in/public/v2/users')
print(x.json())

## result

[{'id': 7530345, 'name': 'Himadri Desai', 'email': 'himadri_desai@orn.example', 'gender': 'male', 'status': 'active'}, {'id': 7530344, 'name': 'Balagopal Agarwal', 'email': 'balagopal_agarwal@rosenbaum.test', 'gender': 'male', 'status': 'active'}, {'id': 7530343, 'name': 'Jagdeep Chattopadhyay', 'email': 'jagdeep_chattopadhyay@schulist.test', 'gender': 'female', 'status': 'inactive'}, {'id': 7530342, 'name': 'Susheel Dwivedi', 'email': 'susheel_dwivedi@rohan-nikolaus.test', 'gender': 'female', 'status': 'inactive'}, {'id': 7530341, 'name': 'Charak Joshi', 'email': 'joshi_charak@glover.test', 'gender': 'female', 'status': 'active'}, {'id': 7530340, 'name': 'Shubha Trivedi', 'email': 'shubha_trivedi@koelpin-bartell.example', 'gender': 'female', 'status': 'active'}, {'id': 7530339, 'name': 'Vidya Tandon', 'email': 'tandon_vidya@pfannerstill-kling.example', 'gender': 'male', 'status': 'active'}, {'id': 7530338, 'name': 'Bankim Arora', 'email': 'arora_bankim@carter.example', 'gender': 'female', 'status': 'active'}, {'id': 7530337, 'name': 'Gautami Gandhi', 'email': 'gautami_gandhi@schoen.test', 'gender': 'female', 'status': 'active'}, {'id': 7530336, 'name': 'Mohinder Singh', 'email': 'mohinder_singh@funk.example', 'gender': 'female', 'status': 'active'}]
