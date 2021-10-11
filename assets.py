import requests
import pprint

params = {
    'collection': 'mutant-ape-yacht-club',
    'limit': 1
    #boredapeyachtclub
    #bored-ape-kennel-club
}
r = requests.get("https://api.opensea.io/api/v1/assets", params=params)

pprint.pprint(r.json())