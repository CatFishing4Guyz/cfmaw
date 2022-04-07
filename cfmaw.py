import requests
import json

class PlayerS1:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s1/Api/Player/{tag}"

    def getInfo(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        name = self.jsonInfo["avatar"]["name"]
        league = self.jsonInfo["avatar"]["league"]
        mainTrophies = str(self.jsonInfo["avatar"]["mainTrophies"]) # Convert to string
        townHallLevels = str(self.jsonInfo["avatar"]["townHallLevels"]["main"]) # Convert to string
        level = str(self.jsonInfo["avatar"]["level"]) # Convert to string
        clanTag = str(self.jsonInfo["clanTag"]) # Convert to string
        createTime = self.jsonInfo["analytics"]["createTime"]

        return "Name: "+name+"\nLeague: "+league+"\nTrophies: "+mainTrophies+"\nTown Hall: "+townHallLevels+"\nLevel: "+level+"\nClan Tag: "+clanTag+"\nCreation Time: "+createTime

    def getLeague(self):
        self.leagueIcon = self.jsonInfo["avatar"]["leagueIcon"]

        return self.leagueIcon

        
class PlayerS2:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s2/Api/Player/{tag}"

    def getInfo(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        name = self.jsonInfo["avatar"]["name"]
        league = self.jsonInfo["avatar"]["league"]
        mainTrophies = str(self.jsonInfo["avatar"]["mainTrophies"]) # Convert to string
        townHallLevels = str(self.jsonInfo["avatar"]["townHallLevels"]["main"]) # Convert to string
        level = str(self.jsonInfo["avatar"]["level"]) # Convert to string
        clanTag = str(self.jsonInfo["clanTag"]) # Convert to string
        createTime = self.jsonInfo["analytics"]["createTime"]

        return "Name: "+name+"\nLeague: "+league+"\nTrophies: "+mainTrophies+"\nTown Hall: "+townHallLevels+"\nLevel: "+level+"\nClan Tag: "+clanTag+"\nCreation Time: "+createTime

    def getLeague(self):
        self.leagueIcon = self.jsonInfo["avatar"]["leagueIcon"]

        return self.leagueIcon

class ClanS1:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s1/Api/Clan/{tag}"

    def getInfo(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonInfo = json.loads(response.content)

        name = jsonInfo["info"]["name"]
        level = str(jsonInfo["info"]["level"]) # Convert to string
        mainTrophies = str(jsonInfo["info"]["mainTrophies"]) # Convert to string
        inviteType = jsonInfo["info"]["type"]
        warFrequency = jsonInfo["info"]["warFrequency"]
        requiredTrophies = str(jsonInfo["info"]["requiredTrophies"]) # Convert to string
        requiredTownHallLevel = str(jsonInfo["info"]["requiredTownHallLevel"]) # Convert to string
        chatLocales = jsonInfo["info"]["chatLocales"]

        return "Name: "+name+"\nLevel: "+level+"\nTrophies: "+mainTrophies+"\nInvite Type: "+inviteType+"\nWar Frequency: "+warFrequency+"\nRequired Trophies: "+requiredTrophies+"\nRequired Town Hall Level: "+requiredTownHallLevel+"\nLanguage: "+chatLocales

class ClanS2:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s2/Api/Clan/{tag}"

    def getInfo(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonInfo = json.loads(response.content)

        name = jsonInfo["info"]["name"]
        level = str(jsonInfo["info"]["level"]) # Convert to string
        mainTrophies = str(jsonInfo["info"]["mainTrophies"]) # Convert to string
        inviteType = jsonInfo["info"]["type"]
        warFrequency = jsonInfo["info"]["warFrequency"]
        requiredTrophies = str(jsonInfo["info"]["requiredTrophies"]) # Convert to string
        requiredTownHallLevel = str(jsonInfo["info"]["requiredTownHallLevel"]) # Convert to string
        chatLocales = jsonInfo["info"]["chatLocales"]

        return "Name: "+name+"\nLevel: "+level+"\nTrophies: "+mainTrophies+"\nInvite Type: "+inviteType+"\nWar Frequency: "+warFrequency+"\nRequired Trophies: "+requiredTrophies+"\nRequired Town Hall Level: "+requiredTownHallLevel+"\nLanguage: "+chatLocales

# Remove the triple quotes to see it in action
"""
tag = input("Enter a random S2 player tag (A hashtag will result in an error): \n")
playerS2 = PlayerS2(tag)
get = playerS2.getInfo()
print(get)
"""
