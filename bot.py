import discord
import os
import sys
import asyncio
import pydustry
from discord.ext import tasks,commands

client = discord.Client()

client = commands.Bot(command_prefix = ':')

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="Я шизоид.(Копия дарка)"))
        await asyncio.sleep(30)
        await client.change_presence(activity=discord.Game(name="Пока дарк делает плагины, я страдаю фигней"))
        await asyncio.sleep(30)

@client.event
async def on_ready():
    client.loop.create_task(status_task())

@client.command()
@commands.has_permissions(administrator=True)
async def say(ctx,*, message=None):
    await ctx.message.delete()
    if message.author.id == '530103444946812929':
        while True:
            await ctx.send(message)
            asyncio.sleep(0.7)

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
async def stop(ctx):
    if message.author.id == '530103444946812929':
        await ctx.send("Stopped.")
        restart_bot()
    else:
        ctx.send("Права на эту команду имеет только <@530103444946812929>")

@client.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx,*, message):
    await ctx.message.delete()
    embed=discord.Embed()
    embed.add_field(name="Embed", value=f"{message}", inline=False)
    await ctx.send(embed=embed)
    
@client.remove_command("help")

@client.command(pass_context=True)
async def ping(ctx):
        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        ping = round((time_2-time_1)*1000)
        await ctx.send(f"ping = {ping}")

client.run('ODYxNTQxMjg3MTYxMTAyMzc2.YOLS2Q.ehatCiqePEhDB5I06kwJUKlqVLw')
