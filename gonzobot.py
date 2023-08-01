import discord
import os
from discord.ext import commands

discordtoken = os.getenv('pytoken')
print(os.getenv('pytoken'))
sliced_token = discordtoken.split(':')[1]
sliced_token = sliced_token.replace('}', '').replace('"', '')
print(sliced_token)
str(sliced_token)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("pee")

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def kick(ctx, member: commands.MemberConverter):
    await ctx.guild.kick(member)
    await ctx.send(f'{member} has been kicked.')


bot.run(sliced_token)











