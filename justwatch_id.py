import json
import requests
import sys

with open('movie_ids.json', 'r') as f:
    # Load the contents of the file as a dictionary
    movies = json.load(f)

# Set up the JustWatch API endpoints and search parameters
justwatch_api_url = 'https://api.justwatch.com'
justwatch_search_url = f'{justwatch_api_url}/content/titles/en_US/popular'

if len(sys.argv) > 1:
    movie_title = " ".join(sys.argv[1:])
else:
    movie_title = input('Enter a movie title: ')

if not movie_title in movies:
    # Make a POST request to the JustWatch API to search for the movie
    payload = {'query': movie_title}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(justwatch_search_url, data=json.dumps(payload), headers=headers, params={})

    # Parse the response JSON and extract the first search result
    # print(response)
    results = json.loads(response.text)['items']
    if len(results) > 0:
        result = results[0]
    else:
        print('No results found.')
        exit()

    movie_title = result['title']
    movies[movie_title] = result['id']

    # Open a file for writing
    with open('movie_ids.json', 'w') as file:
        # Write JSON data to the file
        json.dump(movies, file)

# Print the movie title and ID
# print(f'Movie title: {movie_title}')
# print(f'JustWatch ID: {movies[movie_title]}')
print(movies[movie_title])
