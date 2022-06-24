import os
import time
import nextcord
import platform
import logging
from utils import config
from utils.log import info, error
from utils.bot import get_prefix
from colorama import init
from nextcord.ext import commands
from utils import MongoM

tStart = time.time()
token = config.get("token")
init(autoreset=True)

intents = nextcord.Intents.all()
owner_ids = [580631356485402639, 530103444946812929, 674647047831420975]
client = commands.Bot(command_prefix=get_prefix, intents=intents, owner_ids=owner_ids)
client.remove_command('help')
logging.getLogger('nextcord').setLevel(logging.WARNING)

for dir in os.listdir("commands"):
    for file in os.listdir("commands/" + dir):
        if file.endswith(".py"):
            exec("from commands." + dir + " import " + file.replace(".py", "") + " as command")
            try:
                client.add_command(command.setup(client))
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to load command {file}: {exception}")
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
    info(f"Logged in as client.user.name, Guilds: b({len(client.guilds)}b)")
    info(f"NextCord version: b({nextcord.__version__}b)")
    info(f"Python version: b({platform.python_version()}b)")
    info(f"Running on: b({platform.system()} {platform.release()}b)")
    info(f"Time elapsed: b({tElapsed}b)")

if __name__ in ["__main__"]:
    client.load_extension("jishaku")
    client.run(token)



