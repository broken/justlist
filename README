# JustList

Series of short scripts for comparing Trakt watchlist to viewing providers (data
from JustWatch).

## How to Run

### Initial Setup

After cloning the repo, get Trakt API keys for your account, and populate these
in a file named `.trakt_creds.json`.

```
{
  "client_id": "<client_id>",
  "secret_key": "<secret_key>"
}
```

Next, run `justwatch_providers.py` to populate the `providers.json` file, and
run `trakt_watchlist.py` to populate the `watchlist.json` file.

### Execute

Simply run `main.py` and it will print the movies and providers. The data is
cached in json files, so subsequent runs will not peg the APIs, but you can
`grep` results to your hearts content.

Note that I have yet to add any timeouts to prevent being cut-off from too many
requests to JustWatch, so be advised if your list is long.

### Later calls

Since everything is cached in json files, you will want to rerun `trakt_watchlist.py`
if you have updates to it. You can also delete `movie_providers.json` if you
believe that data needs updating.

## The Scripts

### justwatch_id.py

updates the movie_ids.json file with the justwatch id of a given movie file.

### justwatch_info.py

updates the movie_providers.json file with the current providers of a given movie.

### justwatch_providers.py

writes the justwatch metadata of all providers to the providers.json file.

### trak_watchlist.py

write out your watchlist to trakt_watchlist.py.

### main.py

uses the json files above to print out your movies from your trakt watchlist, and
the available providers you are able to watch it on. If the movie is not
populated in the movie_ids.json or movie_providers.json, it will call the necessary
scripts above.

## Sample output

```
$ python main.py  | grep -i netflix | head -1
Dracula Untold, Apple TV (buy), Apple TV (rent), Google Play Movies (buy), Google Play Movies (rent), Vudu (buy), Vudu (rent), Netflix (flatrate), Amazon Video (buy), Amazon Video (rent), Microsoft Store (buy), Microsoft Store (rent), YouTube (buy), YouTube (rent), Redbox (buy), Redbox (rent), AMC on Demand (buy), AMC on Demand (rent), DIRECTV (buy), DIRECTV (rent)
```
