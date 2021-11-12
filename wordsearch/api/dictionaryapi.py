from os import error
import requests
import json

def dictionaryAPI(word):
    # free open API
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word

    response = requests.request("GET", url)
    cleaned_response = json.loads(response.text)  

    if type(cleaned_response) != list:
        return error
    else:
        return cleaned_response[0]['meanings'][0]['definitions'][0]['definition']

# example response
# [
#     {
#       "word": "hello",
#       "phonetics": [
#         {
#           "text": "/həˈloʊ/",
#           "audio": "https://lex-audio.useremarkable.com/mp3/hello_us_1_rr.mp3"
#         },
#         {
#           "text": "/hɛˈloʊ/",
#           "audio": "https://lex-audio.useremarkable.com/mp3/hello_us_2_rr.mp3"
#         }
#       ],
#       "meanings": [
#         {
#           "partOfSpeech": "exclamation",
#           "definitions": [
#             {
#               "definition": "Used as a greeting or to begin a phone conversation.",
#               "example": "hello there, Katie!"
#             }
#           ]
#         },
#         {
#           "partOfSpeech": "noun",
#           "definitions": [
#             {
#               "definition": "An utterance of “hello”; a greeting.",
#               "example": "she was getting polite nods and hellos from people",
#               "synonyms": [
#                 "greeting",
#                 "welcome",
#                 "salutation",
#                 "saluting",
#                 "hailing",
#                 "address",
#                 "hello",
#                 "hallo"
#               ]
#             }
#           ]
#         },
#         {
#           "partOfSpeech": "intransitive verb",
#           "definitions": [
#             {
#               "definition": "Say or shout “hello”; greet someone.",
#               "example": "I pressed the phone button and helloed"
#             }
#           ]
#         }
#       ]
#     }
#   ]