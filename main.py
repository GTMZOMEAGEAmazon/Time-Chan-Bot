import discord
from discord.ext.commands import *
bot = Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Login : {bot.user}")
@bot.command()
async def ping(ctx):
    await ctx.send("Pong")
bot.run("MTAxMzcyMDkyMjMxMTYzNDk0NA.GuNNxw.ZPdvAG7SumrMS4t-SsxPbSqXrpUh9nOy2Zfsj4")
