import discord
import os
import platform
import sys
import psutil
import asyncio
from discord.ext import tasks,commands

client = discord.Client()
client = commands.Bot(command_prefix = '$')
client.remove_command('help')

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
        await client.change_presence(activity=discord.Game(name="$help"))
        await asyncio.sleep(30)
        await client.change_presence(activity=discord.Game(name="I'm love Discord!"))
        await asyncio.sleep(30)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(title='Ошибка', description=f'**{ctx.author.name}**, Команда не найдена!', color=0xFF0000))
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed = discord.Embed(title='Ошибка', description=f'**{ctx.author.name}**, У вас нет прав для использования этой команды.', color=0xFF0000))
@client.event
async def on_message(ctx):
    if message.content == 'Ня':
        await ctx.send("Ня")
    if message.content == 'ня':
        await ctx.send("Ня")
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    client.loop.create_task(status_task())

client.run('ODYxNTQxMjg3MTYxMTAyMzc2.YOLS2Q.Ja9sfwWISOUKDVdtcIsboP8JZ3k')
