import discord
from discord.ext.commands import *
bot = Bot(command_prefix="!", intents = discord.Intents.all())


@bot.event
async def on_ready():
    print(f"Login : {bot.user}")
@bot.command()
async def ping(ctx):
    await ctx.send("Pong")
bot.run("your_token")
