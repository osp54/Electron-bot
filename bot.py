import time

tStart = time.time()
import discord
import os
import platform
import sys
import asyncio
import jishaku
import colorama
import json
import logging
import pendulum #аналог датетайма
from colorama import init, Fore, Back, Style
from config import settings
from discord.ext import tasks,commands

init(autoreset=True)
intents = discord.Intents.all()
owners = [580631356485402639, 530103444946812929, 674647047831420975]
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix = get_prefix, intents=intents, owner_ids = set(owners))
client.remove_command('help')

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)

def info(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.BLUE}[{Fore.RESET}{now.day}:{now.hour}:{now.minute}:{now.second}{Fore.BLUE}] " + Fore.BLUE + f"[I] {Fore.RESET}" + desc)
def error(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.RED}[{Fore.RESET}{now.day}:{now.hour}:{now.minute}:{now.second}{Fore.RED}] " + Fore.RED + f"[E] " + desc)

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
    info(f"{Fore.CYAN}--------------------------------------------------")
    info(f"Logged in as {client.user.name}")
    info(f"Discord.py API version: {discord.__version__}")
    info(f"Python version: {platform.python_version()}")
    info(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    info(f"Time elapsed: {tElapsed}")
    info(f"{Fore.CYAN}--------------------------------------------------")
    client.loop.create_task(status_task())

if __name__ == "__main__":
    load_extensions("./cogs") #когсы команд
    info("Loaded all extensions from /cogs")
    load_extensions("./utils") #когсы утилит/ивентов
    info("Loaded all extensions from /utils")
client.run(settings['token'])
