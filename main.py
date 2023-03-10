import json
from requests_oauthlib import OAuth2Session
import requests
import subprocess

with open('watchlist.json', 'r') as f:
    # Load the contents of the file as a dictionary
    watchlist = json.load(f)

with open('providers.json', 'r') as f:
    # Load the contents of the file as a dictionary
    providers = json.load(f)

with open('movie_ids.json', 'r') as f:
    # Load the contents of the file as a dictionary
    movies = json.load(f)

with open('movie_providers.json', 'r') as f:
    # Load the contents of the file as a dictionary
    mps = json.load(f)

titles = [item['movie']['title'] for item in watchlist]

watchlist_providers = {}
for title in titles:
  if not title in movies:
    result = subprocess.run('python justwatch_id.py \'' + title + "'", shell=True, check=True, stdout=subprocess.PIPE)
    mid = result.stdout.decode().strip()
  else:
    mid = str(movies[title])
  if not mid in mps:
    subprocess.run('python justwatch_info.py ' + mid, shell=True, check=True, stdout=subprocess.PIPE)
    with open('movie_providers.json', 'r') as f:
        mps = json.load(f)
  out = title
  provider_options = {}
  if mps[mid] is not None:
    for provider in mps[mid]:
      key = f'{providers[str(provider["provider_id"])]["clear_name"]} ({provider["monetization_type"]})'
      provider_options[key] = 1
    for o in provider_options:
      out = f'{out}, {o}'
    print(out)
