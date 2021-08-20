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
def info(desc):
    print(Fore.BLUE + f"[I] {Fore.RESET}" + desc)
#test
info(desc="hmmmm")
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

init(autoreset=True)

intents = discord.Intents.all()
owners = [580631356485402639, 530103444946812929]
client = commands.Bot(command_prefix = commands.when_mentioned and (get_prefix), intents=intents, owner_ids = set(owners))
client.remove_command('help')
#когсы комманд
if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                client.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")
#когсы утилит/ивентов
if __name__ == "__main__":
    for file in os.listdir("./utils"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                client.load_extension(f"utils.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="$ my default prefix"))
        await asyncio.sleep(30)
        await client.change_presence(activity=discord.Game(name="I'm love Discord!"))
        await asyncio.sleep(30)

@client.event
async def on_ready():
    print(f"{Fore.BLUE}Logged in as {client.user.name}")
    print(f"{Fore.BLUE}Discord.py API version: {discord.__version__}")
    print(f"{Fore.BLUE}Python version: {platform.python_version()}")
    print(f"{Fore.BLUE}Running on: {platform.system()} {platform.release()} ({os.name})")
    client.loop.create_task(status_task())

client.run(settings['token'])
