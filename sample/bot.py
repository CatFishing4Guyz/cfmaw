import discord
import cfmaw
import os
from discord import Option, OptionChoice

servers = [
    OptionChoice(name="S1", value="Server 1"),
    OptionChoice(name="S2", value="Server 2")
]

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[831412377869221899], description="Sanity check")
async def player(ctx, server: Option(str, "Pick a server", required=True, choices=servers), tag: Option(str, "Enter a tag, hashtag is optional", required=True)):
    if server == 'S1':
        player = cfmaw.Player('s1', tag)
        info = discord.Embed(title="Some dude's info",
                            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            description=f"Name: {player.name}\nLevel: {player.level}\nClan Tag: {player.clanTag}\nLeague: {player.league}",
                            color=000000)
        info.set_image(url=player.leagueIcon)
        await ctx.respond(embed=info)
    elif server == 'S2':
        player = cfmaw.Player('s2', tag)
        info = discord.Embed(title="Some dude's info",
                            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            description=f"Name: {player.name}\nLevel: {player.level}\nClan Tag: {player.clanTag}\nLeague: {player.league}",
                            color=000000)
        info.set_image(url=player.leagueIcon)
        await ctx.respond(embed=info)
bot.run(os.getenv('THIRD_TOKEN'))
