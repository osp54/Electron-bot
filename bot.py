import time
import nextcord
import os
import platform
#import colorama
import logging
import asyncio
import pymongo
from utils.misc import error, info, get_prefix2, load_extensions
from colorama import init, Fore, Back, Style
from nextcord.ext import commands

tStart = time.time()

mclient = pymongo.MongoClient("mongodb+srv://electron:W$2ov3b$Fff58ludgg@cluster.xyknx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mclient.electron
collg = db.guilds

init(autoreset=True)

intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = get_prefix2, intents=intents, owner_ids = [580631356485402639, 530103444946812929, 674647047831420975])
client.remove_command('help')

logger = logging.getLogger('nextcord')
logger.setLevel(logging.WARNING)

@client.event
async def on_ready():
    modcount = 0
    for guild in client.guilds:
        if collg.count_documents({"_id": guild.id}) == 0:
            collg.insert_one({"_id": guild.id, "lang": "en", "prefix": "$"})
            modcount += 1
    tEnd = time.time()
    tElapsed = tEnd - tStart
    await client.change_presence(activity=nextcord.Game(name=f"$help | Guilds: {len(client.guilds)}"))
    if modcount != 0:
        info(f"Added new {Fore.BLUE}{modcount}{Fore.RESET} guilds to database")
    info(f"Logged in as {Fore.BLUE}{client.user.name}{Fore.RESET}, Guilds: {Fore.BLUE}{len(client.guilds)}")
    info(f"NextCord.py version: {Fore.BLUE}{nextcord.__version__}")
    info(f"Python version: {Fore.BLUE}{platform.python_version()}")
    info(f"Running on: {Fore.BLUE}{platform.system()} {platform.release()} ({os.name})")
    info(f"Time elapsed: {Fore.BLUE}{tElapsed}")

if __name__ == "__main__":
    load_extensions(client, "./cogs") #когсы командc
    client.load_extension("jishaku")
try:
    client.run('ODYxNTQxMjg3MTYxMTAyMzc2.YOLS2Q.ylwKDaLJE4BypVzaLB6Hwai9GHw')
except KeyboardInterrupt as k:
    info("KeyboardInterrupt")
