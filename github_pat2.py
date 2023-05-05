import requests
import getpass

# Set variables
current_token = input('Enter your current token: ') #'<current_personal_access_token>'
description = 'pat2023' #'<description_of_current_token>'
new_description = 'pat2_2023' #'<description_of_new_token>'
new_scopes = ['repo', 'read:user']

# Authenticate with GitHub
username = input("GitHub username: ")
password = getpass.getpass(prompt="GitHub password: ")
auth = (username, password)

# Get current token ID
url = 'https://api.github.com/authorizations'
headers = {'Authorization': f'token {current_token}'}
response = requests.get(url, headers=headers)
response.raise_for_status()
tokens = response.json()
token_id = None

for token in tokens:
    if token['note'] == description:
        token_id = token['id']
        break

if token_id is None:
    print("Token not found")
    exit()

# Revoke current token
url = f'https://api.github.com/authorizations/{token_id}'
response = requests.delete(url, headers=headers)
response.raise_for_status()
print("Current token revoked successfully")

# Generate new token
url = 'https://api.github.com/authorizations'
data = {'note': new_description, 'scopes': new_scopes}
response = requests.post(url, auth=auth, json=data)
response.raise_for_status()
new_token = response.json()['token']
print(f"New token generated: {new_token}")

