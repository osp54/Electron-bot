import discord
import os
import sys
import psutil
import asyncio
import pydustry
from discord.ext import tasks,commands

client = discord.Client()
client = commands.Bot(command_prefix = ':')
tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

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
@commands.has_permissions(manage_messages=True)
async def say(ctx,*, message=None):
    await ctx.message.delete()
    while True:
        await ctx.send(message)

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
@commands.has_permissions(manage_messages=True)
async def stop(ctx):
    await ctx.send("Stopped.")
    restart_bot()

@client.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx,*, message):
    await ctx.message.delete()
    embed=discord.Embed()
    embed.add_field(name="Embed", value=f"{message}", inline=False)
    await ctx.send(embed=embed)
    
@client.remove_command("help")

@client.command(pass_context=True)
async def hostinfo(ctx):
    embh=discord.Embed(title = "Hostinfo(heroku)", description = "Характеристики хоста heroku", color = 0x00A725)
    embh.add_field(name="RAM", value=f"{used_m}MB/{tot_m}MB")
    embh.add_field(name="CPU", value=f"Used: {psutil.cpu_percent()}%")
    await ctx.send(embed=embh)
client.run('ODYxNTQxMjg3MTYxMTAyMzc2.YOLS2Q.ehatCiqePEhDB5I06kwJUKlqVLw')
