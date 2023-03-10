import requests
import json

# Set up the JustWatch API endpoints and search parameters
justwatch_api_url = 'https://api.justwatch.com'
justwatch_search_url = f'{justwatch_api_url}/content/providers/locale/en_US'

# Make a POST request to the JustWatch API to search for the movie
headers = {'Content-Type': 'application/json'}
response = requests.get(justwatch_search_url, headers=headers, params={})

# Parse the response JSON and extract the first search result
results = json.loads(response.text)

new_results = {}
for item in results:
  new_results[item['id']] = item

# Open a file for writing
with open('providers.json', 'w') as file:
    # Write JSON data to the file
    json.dump(new_results, file)
