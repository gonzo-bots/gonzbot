import discord
import os
import json
from discord.ext import commands

token_json = os.getenv('pytoken')
token_dict = json.loads(token_json)
for k, v in token_dict.items():
    discord_token = v
print(discord_token)

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


bot.run(discord_token)











