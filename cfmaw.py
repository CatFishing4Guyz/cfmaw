import requests
import json

class PlayerS1:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s1/Api/Player/{tag}"

    def getInfo(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonInfo = json.loads(response.content)

        createTime = jsonInfo["analytics"]["createTime"]
        bestTrophies = jsonInfo["avatar"]["commodity"]["achievements"]["bestTrophies"]
        league = jsonInfo["avatar"]["league"]
        leagueIcon = jsonInfo["avatar"]["leagueIcon"]
        name = jsonInfo["avatar"]["name"]
        townHallLevels = jsonInfo["avatar"]["townHallLevels"]["main"]
        xp = jsonInfo["avatar"]["xp"]
        clanTag = jsonInfo["clanTag"]

        bestTrophies = str(bestTrophies)
        townHallLevels = str(townHallLevels)
        xp = str(xp)

        return "Name: "+name+"\nLeague: "+league+"\nBest Trophies: "+bestTrophies+"\nCreation Time: "+createTime+"\nTown Hall: "+townHallLevels+"\nXP: "+xp+"\nClan Tag: "+clanTag

class PlayerS2:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s2/Api/Player/{tag}"

    def getInfo(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonInfo = json.loads(response.content)

        createTime = jsonInfo["analytics"]["createTime"]
        bestTrophies = jsonInfo["avatar"]["commodity"]["achievements"]["bestTrophies"]
        league = jsonInfo["avatar"]["league"]
        leagueIcon = jsonInfo["avatar"]["leagueIcon"]
        name = jsonInfo["avatar"]["name"]
        townHallLevels = jsonInfo["avatar"]["townHallLevels"]["main"]
        xp = jsonInfo["avatar"]["xp"]
        clanTag = jsonInfo["clanTag"]

        bestTrophies = str(bestTrophies)
        townHallLevels = str(townHallLevels)
        xp = str(xp)

        return "Name: "+name+"\nLeague: "+league+"\nBest Trophies: "+bestTrophies+"\nCreation Time: "+createTime+"\nTown Hall: "+townHallLevels+"\nXP: "+xp+"\nClan Tag: "+clanTag

class ClanS1:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s1/Api/Clan/{tag}"

    def getInfo(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonInfo = json.loads(response.content)
        dumpedjson = json.dumps(jsonInfo, indent=0, sort_keys=True)
        removeChars = '{[""]},'
        
        for chars in removeChars:
            outputjson = dumpedjson.replace(chars, "")

        return outputjson

# Commented until I find a fix or something, idk
"""
class ClanS2:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s2/Api/Clan/{tag}"

    def getInfo(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonInfo = json.loads(response.content)
        dumpedjson = json.dumps(jsonInfo, indent=0, sort_keys=True)
        removeChars = '{[""]},'

        for chars in removeChars:
            outputjson = dumpedjson.replace(chars, "")

        return outputjson
"""

# Remove the triple quotes to see it in action
"""
playertag = input("Enter a random S2 player tag (A hashtag will result in an error): \n")
tag = playertag
playerS2 = PlayerS2(tag)
get = playerS2.getInfo()
print(get)
"""
