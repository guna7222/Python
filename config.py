BASE_URL = 'https://gorest.co.in'
BASE_PATH = '/public'
VERSION = '/v2'
USERS = '/users'

# helper methods
def get_users():
    return BASE_URL + BASE_PATH + VERSION + USERS

# Authorization
def get_bearer_token():
    return 'Bearer ' + '194132ac555291af78c6b6060e5e0c11b729a7b9bd72c0da3acbc06c302220d3'
