import time
import nextcord
import os
import platform
import logging
from configparser import ConfigParser
from utils.console import info, error, colored
from utils.bot import get_prefix
from colorama import init
from nextcord.ext import commands
from utils import MongoM

cdir = os.path.realpath(__file__).replace("/bot.py", "")

tStart = time.time()
cp = ConfigParser()
cp.read("./config.ini")
token = cp.get("Bot", "token")
init(autoreset=True)

intents = nextcord.Intents.all()
owner_ids = [580631356485402639, 530103444946812929, 674647047831420975]
client = commands.Bot(command_prefix=get_prefix, intents=intents, owner_ids=owner_ids)
client.remove_command('help')
logging.getLogger('nextcord').setLevel(logging.WARNING)

#добавление команд
for dir in os.listdir("commands"):
    for file in os.listdir("commands/" + dir):
        if file.endswith(".py"):
            exec("from commands." + dir + " import " + file.replace(".py", "") + " as command")
            try:
                client.add_command(command.setup(client))
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to load command {file}: {exception}")
#добавление ивентов
for file in os.listdir("events"):
    if file.endswith(".py"):
        exec("from events import " + file.replace(".py", "") + " as event")
        try:
            client.add_listener(event.setup(client))
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            error(f"Failed to load event {file}: {exception}")

@client.event
async def on_ready():
    await MongoM().connect()
    for guild in client.guilds:
        await MongoM().addGuild(guild.id)
    tEnd = time.time()
    tElapsed = tEnd - tStart
    await client.change_presence(activity=nextcord.Game(name=f"$help | Guilds: {len(client.guilds)}"))
    info(f"Logged in as {colored(client.user.name)}, Guilds: {colored(len(client.guilds))}")
    info(f"NextCord version: {colored(nextcord.__version__)}")
    info(f"Python version: {colored(platform.python_version())}")
    info(f"Running on: {colored(platform.system())} {colored(platform.release())} ({colored(os.name)})")
    info(f"Time elapsed: {colored(tElapsed)}")

if __name__ == "__main__":
    client.load_extension("jishaku")
    client.run(token)
