import requests
import json

class Clan:
    def __init__(self, server, tag):
        self.server = server.lower()
        self.tag = tag.strip('#')
        self.url = f"https://api.clashofmagic.cc/magic-{self.server}/clans/{self.tag}"
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        # The stuff
        self.name = self.jsonInfo["info"]["name"]
        self.level = str(self.jsonInfo["info"]["level"])
        self.inviteType = self.jsonInfo["info"]["type"]
        self.builderTrophies = str(self.jsonInfo["info"]["builderTrophies"])
        self.mainTrophies = str(self.jsonInfo["info"]["mainTrophies"])
        self.warFrequency = self.jsonInfo["info"]["warFrequency"]
        self.requiredTrophies = str(self.jsonInfo["info"]["requiredTrophies"])
        self.clanLocation = self.jsonInfo["info"]["clanLocation"]
        self.language = self.jsonInfo["info"]["chatLocales"]
        self.requiredTownHallLevel = str(self.jsonInfo["info"]["requiredTownHallLevel"])
        self.requiredBuilderTrophies = str(self.jsonInfo["info"]["requiredBuilderTrophies"])

class War:
    def __init__(self, server, tag):
        self.server = server.lower()
        self.tag = tag.strip('#')
        self.url = f"https://api.clashofmagic.cc/magic-{self.server}/clans/{self.tag}/currentwar"
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.membersCount = str(self.jsonInfo["membersCount"]) # int
        self.state = self.jsonInfo["state"]
        self.endTime = jsonInfo["warEndTime"]
        self.startTime = jsonInfo["warStartTime"]
        self.duration = jsonInfo["warDuration"]
        self.enemyLevel = str(self.jsonInfo["opponent"]["alliance"]["level"]) # int
        self.enemyName = self.jsonInfo["opponent"]["alliance"]["name"]
        self.enemyTag = self.jsonInfo["opponent"]["alliance"]["tag"]
