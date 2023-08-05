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
async def ping(ctx):
    await ctx.send("pee")

@bot.command(aliases=['holybots ratio', 'holybot\'s ratio', 'hbrat'])
async def holybotsKD(ctx):
    await ctx.send(steamapi.getHolybotsRatio(steamkey))

@bot.command(aliases=['holybots accuracy', 'hbacc'])
async def holybotsAcc(ctx):
    await ctx.send(steamapi.getHolybotsAcc(steamkey))

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def kick(ctx, member: commands.MemberConverter):
    await ctx.guild.kick(member)
    await ctx.send(f'{member} has been kicked.')


bot.run(pytoken)











