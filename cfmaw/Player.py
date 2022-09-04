import requests
import json
        
class Player:
    def __init__(self, server, tag):
        self.server = server.lower()
        self.tag = tag.strip('#')
        __url = f"https://api.clashofmagic.cc/magic-{self.server}/users/{self.tag}"
        __get = requests.get(url = __url, headers = {"accept": "application/json"})
        __player = json.loads(__get.content)
        
        self.name = __player["avatar"]["name"]
        self.league = __player["avatar"]["league"]
        self.clanTag = str(__player["clanTag"]) # convert to string in case someone doesn't have a clan (returns None)
        self.level = str(__player["avatar"]["level"])
        self.builderHallLevel = str(__player["avatar"]["townHallLevels"]["builder"])
        self.townHallLevel = str(__player["avatar"]["townHallLevels"]["main"])
        self.mainTrophies = str(__player["avatar"]["mainTrophies"])
        self.mainAttackLosses = str(__player["avatar"]["statistics"]["mainAttackLosses"])
        self.mainAttackWins = str(__player["avatar"]["statistics"]["mainAttackWins"])
        self.region = __player["region"] # useless
        self.leagueIcon = __player["avatar"]["leagueIcon"]
        self.createTime = __player["analytics"]["createTime"]
        self.tag = __player["tag"] # redundant
        self.builderLosses = str(__player["avatar"]["statistics"]["builderLosses"])
        self.builderDraws = str(__player["avatar"]["statistics"]["builderDraws"])
        self.builderWins = str(__player["avatar"]["statistics"]["builderWins"])
        self.mainDefenseLosses = str(__player["avatar"]["statistics"]["mainDefenseLosses"])
        self.mainDefenseWins = str(__player["avatar"]["statistics"]["mainDefenseWins"])
        self.warStars = str(__player["avatar"]["commodity"]["achievements"]["warStars"])
        self.bestBuilderTrophies = str(__player["avatar"]["commodity"]["achievements"]["bestBuilderTrophies"])
        self.bestTrophies = str(__player["avatar"]["commodity"]["achievements"]["bestTrophies"])

class Token:
    def __init__(self, server, tag, token):
        self.server = server.lower()
        self.tag = tag.strip('#')
        self.token = token
        __url = f"https://api.clashofmagic.cc/magic-{self.server}/users/{self.tag}/verify"
        __get = requests.post(url = __url, headers = {"accept": "application/json", "Content-Type": "application/json"}, data = {"token": self.token})                           
        __token = json.loads(__get.content)

        self.validity = __token["status"]
