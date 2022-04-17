class ClanS2:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s2/clans/{tag}"

    def name(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.name = self.jsonInfo["info"]["name"]
        return self.name

    def level(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.level = str(self.jsonInfo["info"]["level"]) # Convert to string
        return self.level

    def mainTrophies(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.mainTrophies = str(self.jsonInfo["info"]["mainTrophies"]) # Convert to string
        return self.mainTrophies

    def builderTrophies(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.builderTrophies = str(self.jsonInfo["info"]["builderTrophies"]) # Convert to string
        return self.builderTrophies

    def inviteType(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.inviteType = self.jsonInfo["info"]["type"]
        return self.inviteType

    def warFrequency(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.warFrequency = self.jsonInfo["info"]["warFrequency"]
        return self.warFrequency

    def requiredTrophies(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.requiredTrophies = str(self.jsonInfo["info"]["requiredTrophies"]) # Convert to string
        return self.requiredTrophies
    
    def requiredBuilderTrophies(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.requiredBuilderTrophies = str(self.jsonInfo["info"]["requiredBuilderTrophies"]) # Convert to string
        return self.requiredBuilderTrophies

    def requiredTownHallLevel(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.requiredTownHallLevel = str(self.jsonInfo["info"]["requiredTownHallLevel"]) # Convert to string
        return self.requiredTownHallLevel


    def language(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)
        
        self.chatLocales = self.jsonInfo["info"]["chatLocales"]
        return self.chatLocales

    def location(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.clanLocation = self.jsonInfo["info"]["clanLocation"]
        return self.clanLocation

class WarS2:
    def __init__(self, tag):
        self.tag = tag
        self.url = f"https://api.clashofmagic.cc/magic-s2/clans/{self.tag}/currentwar"

    def participantsEach(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.membersCount = str(self.jsonInfo["membersCount"]) # int
        return self.membersCount

    def state(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.state = self.jsonInfo["state"]
        return self.state

    def enemyTag(self): # the keyword is a misnomer, 'alliance' is the enemy
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.enemyTag = self.jsonInfo["teams"]["alliance"]["tag"]
        return self.enemyTag

    def enemyName(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.enemyName = self.jsonInfo["teams"]["alliance"]["name"]
        return self.enemyName

    def enemyLevel(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.enemyLevel = str(self.jsonInfo["teams"]["alliance"]["level"]) # int
        return self.enemyLevel

    def duration(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.duration = jsonInfo["warDuration"]
        return self.duration

    def startTime(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.startTime = jsonInfo["warStartTime"]
        return startTime

    def endTime(self):
        self.response = requests.get(url = self.url, headers = {"accept": "application/json"})
        self.jsonInfo = json.loads(self.response.content)

        self.endTime = jsonInfo["warEndTime"]
        return self.endTime
