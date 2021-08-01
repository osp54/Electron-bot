import discord
import os
import sys
import psutil
import asyncio
from discord.ext import tasks,commands

client = discord.Client()
client = commands.Bot(command_prefix = '$')

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

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="Я шизоид.(Копия дарка)"))
        await asyncio.sleep(30)
        await client.change_presence(activity=discord.Game(name="Пока дарк делает плагины, я страдаю фигней"))
        await asyncio.sleep(30)

@client.event
async def on_ready():
    client.loop.create_task(status_task())

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
@commands.has_permissions(manage_messages=True)
async def restart(ctx):
    await ctx.send("Restarting...")
    restart_bot()
@client.remove_command("help")
