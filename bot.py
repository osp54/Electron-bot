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
import time

tStart = time.time()
init(autoreset=True)
intents = discord.Intents.all()
owners = [580631356485402639, 530103444946812929]
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
client = commands.Bot(command_prefix = commands.when_mentioned and (get_prefix), intents=intents, owner_ids = set(owners))
client.remove_command('help')

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)

def info(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"[{now.day}:{now.hour}:{now.minute}]" + Fore.BLUE + f"[I] {Fore.RESET}" + desc)
def error(desc):
    print(f"[{now.day}:{now.hour}:{now.minute}]" + Fore.RED + f"[E] {Fore.RESET}" + desc)

#загрузить все расширения из папки
def load_extensions(dir):
    for file in os.listdir(dir):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                client.load_extension(f"{dir[2:]}.{extension}")
                info(desc=f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(desc=f"Failed to load extension {extension}\n{exception}")

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
    info(desc=f"Logged in as {client.user.name}")
    info(desc=f"Discord.py API version: {discord.__version__}")
    info(desc=f"Python version: {platform.python_version()}")
    info(desc=f"Running on: {platform.system()} {platform.release()} ({os.name})")
    info(desc=f"{Fore.BLUE}Time elapsed: {tElapsed}")
    client.loop.create_task(status_task())

if __name__ == "__main__":
    load_extensions("./cogs") #когсы команд
    load_extensions("./utils") #когсы утилит/ивентов

client.run(settings['token'])
