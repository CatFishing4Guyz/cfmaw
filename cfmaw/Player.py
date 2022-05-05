import requests
import json
        
class Player:
    def __init__(self, server, tag):
        self.server = server.lower()
        self.tag = tag.strip('#')
        self.url = f"https://api.clashofmagic.cc/magic-{self.server}/users/{self.tag}"
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.name = self.jsonInfo["avatar"]["name"]
        self.league = self.jsonInfo["avatar"]["league"]
        self.clanTag = str(self.jsonInfo["clanTag"]) # Convert to string in case someone doesn't have a clan (returns None)
        self.level = str(self.jsonInfo["avatar"]["level"])
        self.builderHallLevel = str(self.jsonInfo["avatar"]["townHallLevels"]["builder"])
        self.townHallLevel = str(self.jsonInfo["avatar"]["townHallLevels"]["main"])
        self.mainTrophies = str(self.jsonInfo["avatar"]["mainTrophies"])
        self.mainAttackLosses = str(self.jsonInfo["avatar"]["statistics"]["mainAttackLosses"])
        self.mainAttackWins = str(self.jsonInfo["avatar"]["statistics"]["mainAttackWins"])
        self.region = self.jsonInfo["region"] # useless
        self.leagueIcon = self.jsonInfo["avatar"]["leagueIcon"]
        self.createTime = self.jsonInfo["analytics"]["createTime"]
        self.tag = jsonInfo["tag"]
        self.builderLosses = str(self.jsonInfo["avatar"]["statistics"]["builderLosses"])
        self.builderDraws = str(self.jsonInfo["avatar"]["statistics"]["builderDraws"])
        self.builderWins = str(self.jsonInfo["avatar"]["statistics"]["builderWins"])
        self.mainDefenseLosses = str(self.jsonInfo["avatar"]["statistics"]["mainDefenseLosses"])
        self.mainDefenseWins = str(self.jsonInfo["avatar"]["statistics"]["mainDefenseWins"])
        self.warStars = str(self.jsonInfo["avatar"]["commodity"]["achievements"]["warStars"])
        self.bestBuilderTrophies = str(self.jsonInfo["avatar"]["commodity"]["achievements"]["bestBuilderTrophies"])
        self.bestTrophies = str(self.jsonInfo["avatar"]["commodity"]["achievements"]["bestTrophies"]

class Token:
    def __init__(self, server, tag, token):
        self.server = server.lower()
        self.tag = tag.strip('#')
        self.token = token
        self.url = f"https://api.clashofmagic.cc/magic-{self.server}/users/{self.tag}/verify"
        self.response = requests.post(url = self.url, headers = {"accept": "application/json", "Content-Type": "application/json"}, data = {self.token: "string"})                           

        self.validity = json.loads(self.response.content) # returns nonsense if you put an invalid one, can't do anything about it
