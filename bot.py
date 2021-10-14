import time
import nextcord
import os
import platform
import logging
import asyncio
from configparser import ConfigParser
from utils.misc import error, info, get_prefix2, load_extensions
from colorama import init, Fore, Back, Style
from nextcord.ext import commands
from utils import mongo

if "config.ini" not in os.listdir(r"/root/bot"):
    error("config.ini not found. Create it and configure.")
    os.exit()

tStart = time.time()
cp = ConfigParser()
cp.read("/root/bot")
token = cp.get("BOT", "token")
init(autoreset=True)

intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = get_prefix2, intents=intents, owner_ids = [580631356485402639, 530103444946812929, 674647047831420975])
client.remove_command('help')

logger = logging.getLogger('nextcord').setLevel(logging.WARNING)

@client.event
async def on_ready():
    await mongo.MongoM().connect()
    modcount = 0
    for guild in client.guilds:
        await mongo.MongoM().addGuild(guild.id)
    tEnd = time.time()
    tElapsed = tEnd - tStart
    await client.change_presence(activity=nextcord.Game(name=f"$help | Guilds: {len(client.guilds)}"))
    info(f"Logged in as {Fore.BLUE}{client.user.name}{Fore.RESET}, Guilds: {Fore.BLUE}{len(client.guilds)}")
    info(f"NextCord.py version: {Fore.BLUE}{nextcord.__version__}")
    info(f"Python version: {Fore.BLUE}{platform.python_version()}")
    info(f"Running on: {Fore.BLUE}{platform.system()} {platform.release()} ({os.name})")
    info(f"Time elapsed: {Fore.BLUE}{tElapsed}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(load_extensions(client, "./cogs"))
    client.load_extension("jishaku")
    try:
        client.run(token)
    except:
        error("Invalid token.")
        os.exit()
