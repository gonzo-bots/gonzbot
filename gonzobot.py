import discord
import os
import json
from discord.ext import commands
import steamapi

pytoken = json.loads(os.getenv('pytoken'))['pytoken']
steamkey = json.loads(os.getenv('steamkey'))['steamkey']


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def speak(ctx):
    await ctx.send("I track csgo stats.")

@bot.command(aliases=['holybots ratio', 'holybot\'s ratio', 'hbrat'])
async def holybotsKD(ctx):
    await ctx.send(steamapi.getHolybotsRatio(steamkey))

@bot.command(aliases=['holybots accuracy', 'hbacc'])
async def holybotsAcc(ctx):
    await ctx.send(steamapi.getHolybotsAcc(steamkey))

@bot.command(aliases=['holybots maps', 'hbmaps'])
async def holybotsMaps(ctx):
    await ctx.send(steamapi.getHolybotsMaps(steamkey))

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def kick(ctx, member: commands.MemberConverter):
    await ctx.guild.kick(member)
    await ctx.send(f'{member} has been kicked.')

@bot.command()
async def who(ctx):
    if ctx.author.id == 121853574056640516:
        await ctx.send('yes that works')
    else:
        await ctx.send('you are not authorized to use that command')

@bot.command()
async def stats(ctx):
    await ctx.send(steamapi.getUserStats(steamkey, ctx.author.id))






bot.run(pytoken)











