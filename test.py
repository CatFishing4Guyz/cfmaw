import cfmaw 

# Outputs the player name of the tag you entered

tag = input("Enter a player tag (S2): ")
playerS2 = cfmaw.PlayerS2(tag)
print(playerS2.name())


# Outputs the state of a clan, e.g., is it at war?

tag = input("Enter a clan tag (S2): ")
warS2 = cfmaw.WarS2(tag)
print(warS2.state())


# Outputs the clan level

tag = input("Enter a clan tag (S2): ")
clanS2 = cfmaw.ClanS2(tag)
print(clanS2.level())

