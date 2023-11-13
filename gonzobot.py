import discord
import os
import json
from discord.ext import commands

import sentimentanalysis
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
    await ctx.send('I track csgo stats.')

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

@bot.command()
async def analyze(ctx):
    async for message in ctx.message.channel.history(limit=1000):
        if ctx.author.name == message.author.name and message.content.startswith('!') == False:
            with open(f'{message.author}_chat_history.txt', 'a+') as file:
                file.write(message.content + '\n')
    await ctx.send(sentimentanalysis.analyze(f'{ctx.message.author}_chat_history.txt'))

@bot.command()
async def analyzeoth(ctx):
    msg = ctx.message.content.split()
    searchname = msg[1]
    async for message in ctx.message.channel.history(limit=1000):
        if searchname == message.author.name and message.content.startswith('!') == False:
            with open(f'{searchname}_chat_history.txt', 'a+') as file:
                file.write(message.content + '\n')
    await ctx.send(sentimentanalysis.analyze(f'{searchname}_chat_history.txt'))
@bot.command()
async def test(ctx):
    print(ctx.author.name)
    print(ctx.message.content.split())
    async for message in ctx.message.channel.history(limit=1):
        print(message.author.name)
        if ctx.author == message.author:
            print(message.author, ctx.author)
            print(message.author.name)
        if ctx.author == message.author and message.content.startswith('h') == False:
            print('the h was not found')


bot.run(pytoken)











