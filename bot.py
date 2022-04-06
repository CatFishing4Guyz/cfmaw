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

@bot.slash_command(description="Check some dude's S1 info")
async def s1player(ctx, tag: Option(str, "Enter some dude's S1 tag. A hashtag will result in an error.", required = True)):
    playerS1 = PlayerS1(tag)
    get = playerS1.getInfo()

    player=discord.Embed(title="Some dude's info",
                        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                        description=get,
                        color=000000)
    
    await ctx.respond(embed=player)

@bot.slash_command(description="Check some dude's S2 info")
async def s2player(ctx, tag: Option(str, "Enter some dude's S2 tag. A hashtag will result in an error.", required = True)):
    playerS2 = PlayerS2(tag)
    get = playerS2.getInfo()

    player=discord.Embed(title="Some dude's info",
                        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                        description=get,
                        color=000000)
    
    await ctx.respond(embed=player)

@bot.slash_command(description="Check some S1 clan's info")
async def s1clan(ctx, tag: Option(str, "Enter some S1 clan's tag. A hashtag will result in an error.", required = True)):
    clanS1 = ClanS1(tag)
    get = clanS1.getInfo()

    clan=discord.Embed(title="Some clan's info",
                        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                        description=get,
                        color=000000)
    
    await ctx.respond(embed=clan)

@bot.slash_command(description="Check some S2 clan's info")
async def s2clan(ctx, tag: Option(str, "Enter some S2 clan's tag. A hashtag will result in an error.", required = True)):
    clanS2 = ClanS2(tag)
    get = clanS2.getInfo()

    clan=discord.Embed(title="Some clan's info",
                        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                        description=get,
                        color=000000)
    
    await ctx.respond(embed=clan)
    
bot.run(os.getenv('THIRD_TOKEN'))

