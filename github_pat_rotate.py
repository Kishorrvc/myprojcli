import requests
import getpass

# Set variables
token = input("Enter your pat: ") #'<current_personal_access_token>'
headers = {'Authorization': f'token {token}'}
#url = 'https://api.github.com/authorizations'
url = 'https://api.github.com/octocat'

# Get list of existing tokens
response = requests.get(url, headers=headers)
response.raise_for_status()
import pdb; pdb.set_trace()
print(response.text)
tokens = response.json()

# Find the token you want to revoke
token_id = None
for t in tokens:
    if t['note'] == '<description_of_current_token>':
        token_id = t['id']
        break

if token_id is None:
    print("Token not found")
    exit()

# Revoke the old token
response = requests.delete(f'{url}/{token_id}', headers=headers)
response.raise_for_status()

# Generate a new token
username = input("GitHub username: ")
password = getpass.getpass(prompt="GitHub password: ")
scopes = ['repo', 'read:user']
note = '<description_of_new_token>'

response = requests.post(url, headers=headers, auth=(username, password), json={
    'scopes': scopes,
    'note': note
})

response.raise_for_status()
new_token = response.json()['token']
print(f"New token generated: {new_token}")

