import time

tStart = time.time()
import discord
import os
import platform
import colorama
import logging
import asyncio
import jishaku
from functions import error, info, get_prefix
from colorama import init, Fore, Back, Style
from config import settings
from discord.ext import commands

init(autoreset=True)
intents = discord.Intents.all()
owners = [580631356485402639, 530103444946812929, 674647047831420975]
client = commands.Bot(command_prefix = get_prefix, intents=intents, owner_ids = set(owners))
client.remove_command('help')

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)

#загрузить все расширения из папки
def load_extensions(dir):
    for file in os.listdir(dir):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                client.load_extension(f"{dir[2:]}.{extension}")
                info(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to load extension {extension}\n{exception}")

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="$ my default prefix"))
        await asyncio.sleep(30)
        await client.change_presence(activity=discord.Game(name="I'm love Discord!"))
        await asyncio.sleep(30)

@client.event
async def on_ready():
    tEnd = time.time()
    tElapsed = tEnd - tStart
    info(f"Logged in as {client.user.name}")
    info(f"Guilds: {len(client.guilds)}")
    info(f"Discord.py API version: {discord.__version__}")
    info(f"Python version: {platform.python_version()}")
    info(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    info(f"Time elapsed: {tElapsed}")
    client.loop.create_task(status_task())

if __name__ == "__main__":
    client.load_extension("jishaku")
    load_extensions("./cogs") #когсы командc
    info("Loaded all extensions from /cogs")
    load_extensions("./utils") #когсы утилит/ивентов
    info("Loaded all extensions from /utils")
client.run(settings['token'])
