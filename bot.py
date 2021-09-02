import time

tStart = time.time()
import nextcord
import os
import platform
import colorama
import logging
import asyncio
import signal
from functions import error, info, get_prefix
from colorama import init, Fore, Back, Style
from config import settings
from nextcord.ext import commands

init(autoreset=True)
intents = nextcord.Intents.all()
owners = [580631356485402639, 530103444946812929, 674647047831420975]
client = commands.Bot(command_prefix = get_prefix, intents=intents, owner_ids = set(owners))
client.remove_command('help')

logger = logging.getLogger('nextcord')
logger.setLevel(logging.WARNING)

#загрузить все расширения из папки
def load_extensions(dir):
    for file in os.listdir(dir):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                client.load_extension(f"{dir[2:]}.{extension}")
                info(f"Loaded extension {Fore.CYAN}{extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to load extension {Fore.CYAN}{extension}{Fore.RESET}\n{exception}")
def unload_extensions(dir):
    for file in os.listdir(dir):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                client.unload_extension(f"{dir[2:]}.{extension}")
                info(f"Unloaded extension {Fore.CYAN}{extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to unload extension {Fore.CYAN}{extension}{Fore.RESET}\n{exception}")
async def status_task():
    while True:
        await client.change_presence(activity=nextcord.Game(name="$help"))
        await asyncio.sleep(30)
        await client.change_presence(activity=nextcord.Game(name="I'm love discord!"))
        await asyncio.sleep(30)
@client.event
async def on_ready():
    tEnd = time.time()
    tElapsed = tEnd - tStart
    info(f"Logged in as {Fore.CYAN}{client.user.name}{Fore.RESET}, Guilds: {Fore.CYAN}{len(client.guilds)}")
    info(f"NextCord.py version: {Fore.CYAN}{nextcord.__version__}")
    info(f"Python version: {Fore.CYAN}{platform.python_version()}")
    info(f"Running on: {Fore.CYAN}{platform.system()} {platform.release()} ({os.name})")
    info(f"Time elapsed: {Fore.CYAN}{tElapsed}")
    client.loop.create_task(status_task())
if __name__ == "__main__":
    load_extensions("./cogs") #когсы командc
    load_extensions("./utils") #когсы утилит/ивентов
client.run(settings['token'])
