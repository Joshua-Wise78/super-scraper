import discord
import logging
import os
import traceback
from discord.ext import commands
from dotenv import load_dotenv

from jsonUtils import STORAGE_INFO

load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')
ID = os.environ.get('GUILD_ID')

if TOKEN is None:
    raise ValueError("Discord TOKEN is not found.")

if ID is None:
    raise ValueError("Guild ID is not found.")

GUILD_ID = discord.Object(id=ID)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

initial_extensions = [
    'cogs.general'
]

@bot.event
async def on_ready():
    print(f'{bot.user} connected to Discord')
   
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f'Extension loaded: {extension}')
        except Exception as e:
            print(f'Failed to load extension: {extension}. Reason: {e}')
            traceback.print_exc()

    try:
        bot.tree.copy_global_to(guild=GUILD_ID)
        await bot.tree.sync(guild=GUILD_ID)
        print("Synced command(s) to server")
    except Exception as e:
        print(e)
         
if __name__ == "__main__":
    bot.run(TOKEN)
