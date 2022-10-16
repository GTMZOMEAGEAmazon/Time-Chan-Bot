import discord
from discord.ext.commands import *
import os
import json
bot = Bot(command_prefix="!", intents = discord.Intents.all())
with open('hi/config.json', 'r') as f:
    config = json.load(f)
token = config['token']

@bot.event
async def on_ready():
    print(f"Login : {bot.user}")
@bot.command()
async def ping(ctx):
    await ctx.send("Pong")
bot.run("MTAxMzcyMDkyMjMxMTYzNDk0NA.Ge8CWl.qdwuICH-DRp79NHEDLUKbL6IQ6GLMKR7qAl2jU")
