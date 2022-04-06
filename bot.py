import discord
import os
from cfmaw import PlayerS1
from cfmaw import PlayerS2
from cfmaw import ClanS1
from cfmaw import ClanS2
from discord import Option

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Check some dude's info")
async def player(ctx, server: Option(str, 'Choose between "S1" (same as S3) or "S2" (same as S4)', required = True), tag: Option(str, "Enter some dude's tag. A hashtag will result in an error.", required = True)):
    if server == 'S1':
        playerS1 = PlayerS1(tag)
        get = playerS1.getInfo()

        player=discord.Embed(title="Some dude's info",
                            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            description=get,
                            color=000000)
    elif server == 'S2':
        playerS2 = PlayerS2(tag)
        get = playerS2.getInfo()

        player=discord.Embed(title="Some dude's info",
                            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            description=get,
                            color=000000)
    else:
        await ctx.respond("Invalid server. Keep in mind that it's case sensitive.")
    
    await ctx.respond(embed=player)

@bot.slash_command(guild_ids=[831412377869221899, 929320814724124722], description="Check some clan's info")
async def clan(ctx, server: Option(str, 'Choose between "S1" (same as S3) or "S2" (same as S4)', required = True), tag: Option(str, "Enter some clan's tag. A hashtag will result in an error.", required = True)):
    if server == 'S1':
        clanS1 = ClanS1(tag)
        get = clanS1.getInfo()

        clan=discord.Embed(title="Some clan's info",
                            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            description=get,
                            color=000000)
    elif server == 'S2':
        clanS2 = ClanS2(tag)
        get = clanS2.getInfo()

        clan=discord.Embed(title="Some clan's info",
                            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            description=get,
                            color=000000)
    else:
        await ctx.respond("Invalid server. Keep in mind that it's case sensitive.")
    
    await ctx.respond(embed=clan)
    
bot.run(os.getenv('THIRD_TOKEN'))
