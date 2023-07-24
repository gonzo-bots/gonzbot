import discord
import os
from discord.ext import commands




discordtoken = str(os.getenv('PYTOKEN'))
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

'''@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('why does this stop this from working?'):
        await message.channel.send("cause you're dumb")
        '''

@bot.command()
async def kick(ctx, member: commands.MemberConverter):
    await ctx.guild.kick(member)
    await ctx.send(f'{member} has been kicked.')


bot.run(discordtoken)
