import cfmaw 

#=================================================#
# Simple file to demonstrate cfmaw at its finest  #
#=================================================#

# Outputs the player name of the tag you entered
def playerDemo():
    tag = input("Enter a player tag: ")
    server = input("Enter the server the player exists on: ")
    player = cfmaw.Player(server, tag)
    print(player.name)

# Outputs the state of a clan, e.g., is it at war?
def clanWarDemo():
    tag = input("Enter a clan tag: ")
    server = input("Enter the server the clan exists on: ")
    clan = cfmaw.Clan(server, tag)
    print(clan.name)

# Outputs whatever token thing or something, idk
def tokenDemo():
    tag = input("Enter a player tag: ")
    server = input("Enter the server the player exists on: ")
    yourtoken = input("Enter an API token: ")
    token = cfmaw.Token(server, tag, yourtoken)
    print(token.validity)

playerDemo()
clanWarDemo()
tokenDemo()
