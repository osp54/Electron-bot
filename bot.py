import time
import nextcord
import os
import platform
import jishaku
#import colorama
import logging
import asyncio
import sqlite3
from utils.misc import error, info, get_prefix, get_prefix2
from colorama import init, Fore, Back, Style
from nextcord.ext import commands

tStart = time.time()

init(autoreset=True)
try:
  conn = sqlite3.connect(r'db/electron.db')
  cur = conn.cursor()
  conn.execute("""CREATE TABLE IF NOT EXISTS guild (
     ID INTEGER PRIMARY KEY,
     Lang TEXT,
     Prefix TEXT
    )""")
except Exception as e:
  info("SQL not loaded")
  exception = f"{type(e).__name__}: {e}"
  info(exception)

intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = get_prefix2, intents=intents, owner_ids = [580631356485402639, 530103444946812929, 674647047831420975])
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
                info(f"Loaded extension {Fore.BLUE}{extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to load extension {Fore.BLUE}{extension}{Fore.RESET}\n{exception}")
def unload_extensions(dir):
    for file in os.listdir(dir):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                client.unload_extension(f"{dir[2:]}.{extension}")
                info(f"Unloaded extension {Fore.BLUE}{extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to unload extension {Fore.BLUE}{extension}{Fore.RESET}\n{exception}")

@client.event
async def on_ready():
    tEnd = time.time()
    tElapsed = tEnd - tStart
    await client.change_presence(activity=nextcord.Game(name=f"$help | Guilds: {len(client.guilds)}"))
    info(f"Logged in as {Fore.BLUE}{client.user.name}{Fore.RESET}, Guilds: {Fore.BLUE}{len(client.guilds)}")
    info(f"NextCord.py version: {Fore.BLUE}{nextcord.__version__}")
    info(f"Python version: {Fore.BLUE}{platform.python_version()}")
    info(f"Running on: {Fore.BLUE}{platform.system()} {platform.release()} ({os.name})")
    info(f"Time elapsed: {Fore.BLUE}{tElapsed}")

if __name__ == "__main__":
    load_extensions("./cogs") #когсы командc
    client.load_extension("jishaku")
try:
    client.run(os.environ['TOKEN'])
except KeyboardInterrupt as k:
    info("KeyboardInterrupt")
