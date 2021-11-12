import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

def urbanDict(term):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    querystring = {"term":term}

    headers = {
        'x-rapidapi-host': str(os.getenv('URBAN_DICT_HOST')),
        'x-rapidapi-key': str(os.getenv('URBAN_DICT_KEY'))
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    cleaned_response = json.loads(response.text) 
    if 'error' in cleaned_response:
        return os.error
    else:
        return cleaned_response['list'][0]['definition']

# example object (comes in a list)
# {11 items
# "definition":"The only [proper] [response] to something that makes absolutely [no sense]."
# "permalink":"http://wat.urbanup.com/3322419"
# "thumbs_up":3874
# "sound_urls":[...]3 items
# "author":"watwat"
# "word":"wat"
# "defid":3322419
# "current_vote":""
# "written_on":"2008-09-04T02:15:08.000Z"
# "example":"1: If all the animals on the [equator] were capable of [flattery], Halloween and Easter would fall on the same day.
# 2: wat

# 1: Wow your cock is almost as big as my dad's.
# 2: wat

# 1: I accidentially a whole [coke bottle]
# 2: You accidentially what?
# 1: A whole coke bottle
# 2: wat"
# "thumbs_down":439
# }