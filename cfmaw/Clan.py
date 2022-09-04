import requests
import json

class Clan:
    def __init__(self, server, tag):
        self.server = server.lower()
        self.tag = tag.strip('#')
        __url = f"https://api.clashofmagic.cc/magic-{self.server}/clans/{self.tag}"
        __get = requests.get(url = __url, headers = {"accept": "application/json"})
        __clan = json.loads(__get.content)

        self.name = __clan["info"]["name"]
        self.level = str(__clan["info"]["level"])
        self.inviteType = __clan["info"]["type"]
        self.builderTrophies = str(__clan["info"]["builderTrophies"])
        self.mainTrophies = str(__clan["info"]["mainTrophies"])
        self.warFrequency = __clan["info"]["warFrequency"]
        self.requiredTrophies = str(__clan["info"]["requiredTrophies"])
        self.clanLocation = __clan["info"]["clanLocation"]
        self.language = __clan["info"]["chatLocales"]
        self.requiredTownHallLevel = str(__clan["info"]["requiredTownHallLevel"])
        self.requiredBuilderTrophies = str(__clan["info"]["requiredBuilderTrophies"])

class War:
    def __init__(self, server, tag):
        self.server = server.lower()
        self.tag = tag.strip('#')
        __url = f"https://api.clashofmagic.cc/magic-{self.server}/clans/{self.tag}/currentwar"
        __get = requests.get(url = __url, headers = {"accept": "application/json"})
        __war = json.loads(__get.content)
        
        self.membersCount = str(__war["membersCount"])
        self.state = __war["state"]
        self.endTime = __war["warEndTime"]
        self.startTime = __war["warStartTime"]
        self.duration = __war["warDuration"]
        self.enemyLevel = str(__war["opponent"]["alliance"]["level"])
        self.enemyName = __war["opponent"]["alliance"]["name"]
        self.enemyTag = __war["opponent"]["alliance"]["tag"]
