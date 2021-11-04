import time
import nextcord
import os
import platform
import logging
import asyncio
from configparser import ConfigParser
from utils.console import info, error, colored
from utils.bot import get_prefix, load_extensions
from colorama import init, Fore, Back, Style
from nextcord.ext import commands
from utils import mongo

if os.name != "nt":
    import uvloop
    uvloop.install()

cdir = os.path.realpath(__file__).replace("/bot.py", "")

if "config.ini" not in os.listdir(cdir):
    error("config.ini file not found. Creating this file...")
    with open("config.ini", "w") as config:
        config.write("[Bot]\ntoken = Bot's token.")
        config.close()
        exit()

tStart = time.time()
cp = ConfigParser()
cp.read(cdir + "/config.ini")
token = cp.get("Bot", "token")
init(autoreset=True)

intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = get_prefix, intents=intents, owner_ids = [580631356485402639, 530103444946812929, 674647047831420975])
client.remove_command('help')

logger = logging.getLogger('nextcord').setLevel(logging.WARNING)

@client.event
async def on_ready():
    await mongo.MongoM().connect()
    for guild in client.guilds:
        await mongo.MongoM().addGuild(guild.id)
    tEnd = time.time()
    tElapsed = tEnd - tStart
    await client.change_presence(activity=nextcord.Game(name=f"$help | Guilds: {len(client.guilds)}"))
    info(f"Logged in as {colored(client.user.name)}, Guilds: {colored(len(client.guilds))}")
    info(f"NextCord version: {colored(nextcord.__version__)}")
    info(f"Python version: {colored(platform.python_version())}")
    info(f"Running on: {colored(platform.system())} {colored(platform.release())} ({colored(os.name)})")
    info(f"Time elapsed: {colored(tElapsed)}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(load_extensions(client, cdir + "/cogs"))
    client.load_extension("jishaku")
    try:
        client.run(token)
    except:
        error("Invalid token.")
        exit()