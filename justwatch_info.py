import json
import requests
import sys

with open('movie_providers.json', 'r') as f:
    # Load the contents of the file as a dictionary
    movie_providers = json.load(f)

if len(sys.argv) > 1:
    title_id = sys.argv[1]
else:
    title_id = input('Enter a movie id: ')

# Set up the JustWatch API endpoints and search parameters
justwatch_api_url = 'https://api.justwatch.com'
content_type = 'movie'
locale = 'en_US'
justwatch_search_url = f'{justwatch_api_url}/content/titles/{content_type}/{title_id}/locale/{locale}'
# print(justwatch_search_url)

# Make a POST request to the JustWatch API to search for the movie
headers = {'Content-Type': 'application/json', 'User-Agent': 'JustWatch Python client'}
response = requests.get(justwatch_search_url, headers=headers, params={})

# Parse the response JSON and extract the first search result
# print(response)
# Parse the JSON response to extract the streaming providers
data = response.json()
providers = data.get("offers")
# print(json.dumps(providers, indent=2))

# Print the names of the streaming providers
if providers:
    for provider in providers:
        provider_id = provider.get("provider_id")
        # print(provider_id)
else:
    print("No streaming providers found for this movie")

movie_providers[title_id] = providers

# Open a file for writing
with open('movie_providers.json', 'w') as file:
    # Write JSON data to the file
    json.dump(movie_providers, file)