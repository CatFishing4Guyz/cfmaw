import requests
import json
from pprint import pprint

class PlayerS1:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s1/Api/Player/{tag}"

    def get(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonresponse = response.content
        jsoninfo = json.loads(response.content)

        #pprint(jsoninfo) # not sure which is better tbh
        origjson = json.dumps(jsoninfo, indent=0, sort_keys=True)
        remove_chars = '{[""]},'

        newjson = origjson
        for chars in remove_chars:
            newjson = newjson.replace(chars, "")

        return newjson

class PlayerS2:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s2/Api/Player/{tag}"

    def get(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonresponse = response.content
        jsoninfo = json.loads(response.content)

        #pprint(jsoninfo)
        origjson = json.dumps(jsoninfo, indent=0, sort_keys=True)
        remove_chars = '{[""]},'

        newjson = origjson
        for chars in remove_chars:
            newjson = newjson.replace(chars, "")

        return newjson

class ClanS1:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s1/Api/Clan/{tag}"

    def get(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonresponse = response.content
        jsoninfo = json.loads(response.content)

        #pprint(jsoninfo)
        origjson = json.dumps(jsoninfo, indent=0, sort_keys=True)
        remove_chars = '{[""]},'

        newjson = origjson
        for chars in remove_chars:
            newjson = newjson.replace(chars, "")

        return newjson

class ClanS2:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s2/Api/Clan/%23{tag}"

    def get(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonresponse = response.content
        jsoninfo = json.loads(response.content)

        #pprint(jsoninfo)
        origjson = json.dumps(jsoninfo, indent=0, sort_keys=True)
        remove_chars = '{[""]},'

        newjson = origjson
        for chars in remove_chars:
            newjson = newjson.replace(chars, "")

        return newjson

# Remove the triple quotes to see it in action
"""
playertag = input("Enter a random S2 player tag (hashtag is not needed): \n")
tag = playertag
playerS2 = PlayerS2(tag)
get = playerS2.get()
print(get)
"""
