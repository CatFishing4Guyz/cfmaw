import requests
import json
        
class Player:
    def __init__(self, server, tag):
        self.server = server.lower()
        self.tag = tag.strip('#').lower()
        __url = f"https://api.clashofmagic.cc/magic-{self.server}/users/{self.tag}"
        __get = requests.get(url = __url, headers = {"accept": "application/json"})
        __player = json.loads(__get.content)
        
        # Player
        self.tag = __player["tag"] # redundant
        self.clanTag = str(__player["clanTag"]) # returns None if player doesn't have a clan
        self.region = __player["region"] # useless

            # Analytics
            self.createTime = __player["analytics"]["createTime"]

        # Avatar
        self.name = __player["avatar"]["name"]
        self.level = str(__player["avatar"]["level"])
        self.xp = str(__player["avatar"]["xp"])
        self.league = __player["avatar"]["league"]
        self.leagueIcon = __player["avatar"]["leagueIcon"]
        self.mainTrophies = str(__player["avatar"]["mainTrophies"])
        self.builderTrophies = str(__player["avatar"]["builderTrophies"])
        self.legendaryTrophies = str(__player["avatar"]["legendaryTrophies"])
        self.legendaryTrophiesBuilder = str(__player["avatar"]["legendaryTrophiesBuilder"])

            # Town Hall Levels
            self.townHallLevel = str(__player["avatar"]["townHallLevels"]["main"])
            self.builderHallLevel = str(__player["avatar"]["townHallLevels"]["builder"])

            # Statistics
            self.mainAttackWins = str(__player["avatar"]["statistics"]["mainAttackWins"])
            self.mainAttackLosses = str(__player["avatar"]["statistics"]["mainAttackLosses"])
            self.mainDefenseWins = str(__player["avatar"]["statistics"]["mainDefenseWins"])
            self.mainDefenseLosses = str(__player["avatar"]["statistics"]["mainDefenseLosses"])
            self.builderWins = str(__player["avatar"]["statistics"]["builderWins"])
            self.builderDraws = str(__player["avatar"]["statistics"]["builderDraws"])
            self.builderLosses = str(__player["avatar"]["statistics"]["builderLosses"])
        
        
            # Legend League

                # Best Season
                self.bestSeasonMonth = str(__player["avatar"]["legendLeague"]["bestSeason"]["month"])
                self.bestSeasonYear = str(__player["avatar"]["legendLeague"]["bestSeason"]["year"])
                self.bestSeasonScore = str(__player["avatar"]["legendLeague"]["bestSeason"]["score"])
                self.bestSeasonRank = str(__player["avatar"]["legendLeague"]["bestSeason"]["rank"])

                # Previous Season
                self.previousSeasonMonth = str(__player["avatar"]["legendLeague"]["previousSeason"]["month"])
                self.previousSeasonYear = str(__player["avatar"]["legendLeague"]["previousSeason"]["year"])
                self.previousSeasonScore = str(__player["avatar"]["legendLeague"]["previousSeason"]["score"])
                self.previousSeasonRank = str(__player["avatar"]["legendLeague"]["previousSeason"]["rank"])

            # Commodity

                # Achievements
                self.bestTrophies = str(__player["avatar"]["commodity"]["achievements"]["bestTrophies"])
                self.bestBuilderTrophies = str(__player["avatar"]["commodity"]["achievements"]["bestBuilderTrophies"])
                self.warStars = str(__player["avatar"]["commodity"]["achievements"]["warStars"])

class Token:
    def __init__(self, server, tag, token):
        self.server = server.lower()
        self.tag = tag.strip('#').lower()
        self.token = token.lower()
        __url = f"https://api.clashofmagic.cc/magic-{self.server}/users/{self.tag}/verify"
        __get = requests.post(url = __url, headers = {"accept": "application/json", "Content-Type": "application/json"}, data = {"token": self.token})                           
        __token = json.loads(__get.content)

        # Token
        self.validity = __token["status"]