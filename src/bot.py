import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from keep_alive import keep_alive

load_dotenv()

DISCORD_TOKEN: str = os.getenv('TOKEN')

print(DISCORD_TOKEN)

intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)

@bot.event
async def on_ready():
    print(f'logged as {bot.user} 🌰🐿️')

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

keep_alive()
bot.run(DISCORD_TOKEN)
