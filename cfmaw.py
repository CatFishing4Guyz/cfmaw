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
        mainTrophies = str(jsonInfo["avatar"]["mainTrophies"])
        league = jsonInfo["avatar"]["league"]
        leagueIcon = jsonInfo["avatar"]["leagueIcon"]
        name = jsonInfo["avatar"]["name"]
        townHallLevels = str(jsonInfo["avatar"]["townHallLevels"]["main"])
        level = str(jsonInfo["avatar"]["level"])
        clanTag = str(jsonInfo["clanTag"])

        # Storing the league in a variable until I find something to do with it
        league = jsonInfo["avatar"]["league"]

        return "Name: "+name+"\nLeague: "+league+"\nTrophies: "+mainTrophies+"\nCreation Time: "+createTime+"\nTown Hall: "+townHallLevels+"\nLevel: "+level+"\nClan Tag: "+clanTag
        
class PlayerS2:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s2/Api/Player/{tag}"

    def getInfo(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonInfo = json.loads(response.content)

        createTime = jsonInfo["analytics"]["createTime"]
        mainTrophies = str(jsonInfo["avatar"]["mainTrophies"])
        league = jsonInfo["avatar"]["league"]
        leagueIcon = jsonInfo["avatar"]["leagueIcon"]
        name = jsonInfo["avatar"]["name"]
        townHallLevels = str(jsonInfo["avatar"]["townHallLevels"]["main"])
        level = str(jsonInfo["avatar"]["level"])
        clanTag = str(jsonInfo["clanTag"])

        league = jsonInfo["avatar"]["league"]

        return "Name: "+name+"\nLeague: "+league+"\nTrophies: "+mainTrophies+"\nCreation Time: "+createTime+"\nTown Hall: "+townHallLevels+"\nLevel: "+level+"\nClan Tag: "+clanTag

class ClanS1:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s1/Api/Clan/{tag}"

    def getInfo(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonInfo = json.loads(response.content)

        chatLocales = jsonInfo["info"]["chatLocales"]
        level = str(jsonInfo["info"]["level"])
        mainTrophies = str(jsonInfo["info"]["mainTrophies"])
        name = jsonInfo["info"]["name"]
        requiredTownHallLevel = str(jsonInfo["info"]["requiredTownHallLevel"])
        requiredTrophies = str(jsonInfo["info"]["requiredTrophies"])
        tags = jsonInfo["info"]["tags"]
        inviteType = jsonInfo["info"]["type"]
        warFrequency = jsonInfo["info"]["warFrequency"]

        return "Name: "+name+"\nLevel: "+level+"\nTrophies: "+mainTrophies+"\nInvite Type: "+inviteType+"\nWar Frequency: "+warFrequency+"\nRequired Trophies: "+requiredTrophies+"\nRequired Town Hall Level: "+requiredTownHallLevel+"\nLanguage: "+chatLocales

class ClanS2:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s2/Api/Clan/{tag}"

    def getInfo(self):
        response = requests.get(url = self.url, headers = {"accept": "application/json"})
        jsonInfo = json.loads(response.content)

        chatLocales = jsonInfo["info"]["chatLocales"]
        level = str(jsonInfo["info"]["level"])
        mainTrophies = str(jsonInfo["info"]["mainTrophies"])
        name = jsonInfo["info"]["name"]
        requiredTownHallLevel = str(jsonInfo["info"]["requiredTownHallLevel"])
        requiredTrophies = str(jsonInfo["info"]["requiredTrophies"])
        tags = jsonInfo["info"]["tags"]
        inviteType = jsonInfo["info"]["type"]
        warFrequency = jsonInfo["info"]["warFrequency"]

        return "Name: "+name+"\nLevel: "+level+"\nTrophies: "+mainTrophies+"\nInvite Type: "+inviteType+"\nWar Frequency: "+warFrequency+"\nRequired Trophies: "+requiredTrophies+"\nRequired Town Hall Level: "+requiredTownHallLevel+"\nLanguage: "+chatLocales

# Remove the triple quotes to see it in action
"""
playertag = input("Enter a random S2 player tag (A hashtag will result in an error): \n")
tag = playertag
playerS2 = PlayerS2(tag)
get = playerS2.getInfo()
print(get)
"""
