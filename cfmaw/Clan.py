import requests
import json

class Clan:
    def __init__(self, server, tag):
        self.server = server.lower()
        self.tag = tag.strip('#').lower()
        __url = f"https://api.clashofmagic.cc/magic-{self.server}/clans/{self.tag}"
        __get = requests.get(url = __url, headers = {"accept": "application/json"})
        __clan = json.loads(__get.content)

        # Clan
        self.tag = __clan["tag"]

            # Info
            self.name = __clan["info"]["name"]
            self.description = __clan["info"]["description"]
            self.level = str(__clan["info"]["level"])
            self.xp = str(__clan["info"]["xp"])
            self.type = __clan["info"]["type"]
            self.clanLocation = __clan["info"]["clanLocation"]
            self.language = __clan["info"]["chatLocales"]
            self.warFrequency = __clan["info"]["warFrequency"]
            self.mainTrophies = str(__clan["info"]["mainTrophies"])
            self.builderTrophies = str(__clan["info"]["builderTrophies"])
            self.requiredTrophies = str(__clan["info"]["requiredTrophies"])
            self.requiredBuilderTrophies = str(__clan["info"]["requiredBuilderTrophies"])
            self.requiredTownHallLevel = str(__clan["info"]["requiredTownHallLevel"])
            self.publicWarLogEnabled = str(__clan["info"]["publicWarLogEnabled"])
            self.friendlyWarsEnabled = str(__clan["info"]["friendlyWarsEnabled"])
            self.warStatistics = str(__clan["info"]["warStatistics"])

                # Tags
                self.firstTag = str(__clan["info"]["tags"][0])
                self.secondTag = str(__clan["info"]["tags"][1])
                self.thirdTag = str(__clan["info"]["tags"][2])

class War:
    def __init__(self, server, tag):
        self.server = server.lower()
        self.tag = tag.strip('#').lower()
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
