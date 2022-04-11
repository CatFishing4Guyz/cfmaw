import requests
import json
        
class PlayerS1:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s1/Api/Player/{tag}"

    def name(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.name = self.jsonInfo["avatar"]["name"]
        return self.name

    def league(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.league = self.jsonInfo["avatar"]["league"]
        return self.league

    def trophies(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.mainTrophies = str(self.jsonInfo["avatar"]["mainTrophies"]) # Convert to string
        return self.mainTrophies

    def townHallLevel(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.townHallLevel = str(self.jsonInfo["avatar"]["townHallLevels"]["main"]) # Convert to string
        return self.townHallLevel

    def builderHallLevel(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.builderHallLevel = str(self.jsonInfo["avatar"]["townHallLevels"]["builder"])
        return self.builderHallLevel

    def level(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.level = str(self.jsonInfo["avatar"]["level"]) # Convert to string
        return self.level

    def clanTag(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.clanTag = str(self.jsonInfo["clanTag"]) # Convert to string in case someone doesn't have a clan (returns None)
        return self.clanTag

    def createTime(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.createTime = self.jsonInfo["analytics"]["createTime"]
        return self.createTime

    def leagueIcon(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.leagueIcon = self.jsonInfo["avatar"]["leagueIcon"]
        return self.leagueIcon

    def region(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.region = self.jsonInfo["region"]

    def mainAttackWins(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.mainAttackWins = str(self.jsonInfo["avatar"]["statistics"]["mainAttackWins"])
        return self.mainAttackWins

    def mainAttackLosses(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.mainAttackLosses = str(self.jsonInfo["avatar"]["statistics"]["mainAttackLosses"])
        return self.mainAttackLosses

    def mainDefenseWins(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.mainDefenseWins = str(self.jsonInfo["avatar"]["statistics"]["mainDefenseWins"])
        return self.mainDefenseWins

    def mainDefenseLosses(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.mainDefenseLosses = str(self.jsonInfo["avatar"]["statistics"]["mainDefenseLosses"])
        return self.mainDefenseLosses

    def builderWins(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.builderWins = str(self.jsonInfo["avatar"]["statistics"]["builderWins"])
        return self.builderWins

    def builderDraws(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.builderDraws = str(self.jsonInfo["avatar"]["statistics"]["builderDraws"])
        return self.builderDraws

    def builderLosses(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.builderLosses = str(self.jsonInfo["avatar"]["statistics"]["builderLosses"])
        return self.builderLosses

    def tag(self): # redundant but i'll add it anyway
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.tag = jsonInfo["tag"]

    def xp(self): # useless but i'll add it anyway
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.xp = jsonInfo["avatar"]["xp"]
        return xp

    def bestTrophies(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.bestTrophies = str(self.jsonInfo["avatar"]["commodity"]["achievements"]["bestTrophies"])
        return self.bestTrophies

    def bestBuilderTrophies(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.bestBuilderTrophies = str(self.jsonInfo["avatar"]["commodity"]["achievements"]["bestBuilderTrophies"])
        return self.bestBuilderTrophies

    def warStars(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.warStars = str(self.jsonInfo["avatar"]["commodity"]["achievements"]["warStars"])
        return self.warStars
