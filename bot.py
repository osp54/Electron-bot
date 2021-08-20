import discord
import os
import platform
import sys
import asyncio
import jishaku
import colorama
import json
from colorama import init, Fore, Back, Style
from config import settings
from discord.ext import tasks,commands
import time

tStart = time.time()

def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

init(autoreset=True)

def info(desc):
    print(Fore.BLUE + f"[I] {Fore.RESET}" + desc)
def error(desc):
    print(Fore.RED + f"[E] {Fore.RESET}" + desc)

intents = discord.Intents.all()
owners = [580631356485402639, 530103444946812929]
client = commands.Bot(command_prefix = commands.when_mentioned and (get_prefix), intents=intents, owner_ids = set(owners))
client.remove_command('help')
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

#когсы комманд
if __name__ == "__main__":
    load_extensions("./cogs")
    load_extensions("./utils")

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

client.run(settings['token'])
