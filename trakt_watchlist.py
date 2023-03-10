import requests
import json
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Replace <TRAKT_USERNAME> with your Trakt.tv username
trakt_username = 'trakt@robertneale.com'

# Replace <TRAKT_CLIENT_ID> and <TRAKT_CLIENT_SECRET> with your Trakt.tv API credentials
with open('credentials.json') as f:
    trakt_creds = json.load(f)
    trakt_client_id = trakt_creds['client_id']
    trakt_client_secret = trakt_creds['secret_key']

# Set up the OAuth2Session object with the Trakt.tv API endpoints and your credentials
trakt_api_url = 'https://api.trakt.tv'
trakt_authorize_url = f'{trakt_api_url}/oauth/authorize'
trakt_token_url = f'{trakt_api_url}/oauth/token'
trakt_session = OAuth2Session(client_id=trakt_client_id, redirect_uri='urn:ietf:wg:oauth:2.0:oob')

# Obtain the authorization URL to authorize the app to access your Trakt.tv account
authorization_url, state = trakt_session.authorization_url(trakt_authorize_url)

print(f'Please visit this URL and grant access to the app: {authorization_url}')
authorization_code = input('Enter the authorization code: ').strip()

# Exchange the authorization code for an access token and refresh token
full_response = f'urn:ietf:wg:oauth:2.0:oob?code={authorization_code}&state={state}'
token = trakt_session.fetch_token(trakt_token_url, client_secret=trakt_client_secret, authorization_response=full_response)

# Make a GET request to the Trakt.tv API to retrieve your watchlist
trakt_watchlist_url = f'{trakt_api_url}/sync/watchlist/movies'
headers = {'Content-Type': 'application/json', 'trakt-api-version': '2', 'Authorization': f'Bearer {token["access_token"]}', 'trakt-api-key': trakt_client_id}
response = requests.get(trakt_watchlist_url, headers=headers)

# Parse the response JSON and extract the movie titles
watchlist = response.json()
titles = [item['movie']['title'] for item in watchlist]

# Open a file for writing
with open('watchlist.json', 'w') as file:
    # Write JSON data to the file
    json.dump(watchlist, file)

# Print the movie titles
print('Your Trakt.tv watchlist:')
for title in titles:
    print(f'- {title}')
