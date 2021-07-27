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
    if message == 'None':
        return
    while True:
        await ctx.send(message)
        asyncio.sleep(0.5)

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
@commands.has_permissions(administrator=True)
async def embed(ctx,*, message):
    await ctx.message.delete()
    embed=discord.Embed()
    embed.add_field(name="Embed", value=f"{message}", inline=False)
    await ctx.send(embed=embed)
#переменные
hub = pydustry.Server('darkdustry.ml', int(6567))
surv = pydustry.Server('darkdustry.ml', int(6000))
attack = pydustry.Server('darkdustry.ml', int(1000))
sand = pydustry.Server('darkdustry.ml', int(2000))
pvp = pydustry.Server('darkdustry.ml', int(4000))
hexed = pydustry.Server('darkdustry.ml', int(3000))
towerdef = pydustry.Server('darkdustry.ml', int(7000))
siege = pydustry.Server('darkdustry.ml', int(8000))
@client.command()
async def server(ctx, server):
    try:
        if server == 'hub':
            embhub = discord.Embed(color = 0x00A725)
            embhub.add_field(name="Статус сервера HUB", value=f"Игроков: {hub.get_status()['players']}\nКарта: {hub.get_status()['map']}")
            embhub.add_field(name="Сервера", value="```hub, survival, attack, sandbox, pvp, hexed, td, siege```")
            await ctx.send(embed=embhub)
        elif server == 'survival':
            embsurv = discord.Embed(color = 0x00A725)
            embsurv.add_field(name="Статус сервера Survival", value=f"Игроков: {surv.get_status()['players']}\nКарта: {surv.get_status()['map']}")
            embsurv.add_field(name="Сервера", value="```hub, survival, attack, sandbox, pvp, hexed, td, siege```")
            await ctx.send(embed=embsurv)
        elif server == 'attack':
            embatk = discord.Embed(color = 0x00A725)
            embatk.add_field(name="Статус сервера Attack", value=f"Игроков: {attack.get_status()['players']}\nКарта: {attack.get_status()['map']}")
            embatk.add_field(name="Сервера", value="```hub, survival, attack, sandbox, pvp, hexed, td, siege```\n:server <server>")
            await ctx.send(embed=embatk)
        elif server == 'sandbox':
            embsand = discord.Embed(color = 0x00A725)
            embsand.add_field(name="Статус сервера Sandbox", value=f"Игроков: {sand.get_status()['players']}\nКарта: {sand.get_status()['map']}")
            embsand.add_field(name="Сервера", value="```hub, survival, attack, sandbox, pvp, hexed, td, siege```")
            await ctx.send(embed=embsand)
        elif server == 'pvp':
            embpvp = discord.Embed(color = 0x00A725)
            embpvp.add_field(name="Статус сервера PvP", value=f"Игроков: {pvp.get_status()['players']}\nКарта: {pvp.get_status()['map']}")
            embpvp.add_field(name="Сервера", value="```hub, survival, attack, sandbox, pvp, hexed, td, siege```")
            await ctx.send(embed=embpvp)
        elif server == 'hexed':
            embhex = discord.Embed(color = 0x00A725)
            embhex.add_field(name="Статус сервера Hexed", value=f"Игроков: {hexed.get_status()['players']}\nКарта: {hexed.get_status()['map']}")
            embhex.add_field(name="Сервера", value="```hub, survival, attack, sandbox, pvp, hexed, td, siege```")
            await ctx.send(embed=embhex)
        elif server == 'td':
            embtd = discord.Embed(color = 0x00A725)
            embtd.add_field(name="Статус сервера Tower Defence", value=f"Игроков: {towerdef.get_status()['players']}\nКарта: {towerdef.get_status()['map']}")
            embtd.add_field(name="Сервера", value="```hub, survival, attack, sandbox, pvp, hexed, td, siege```")
            await ctx.send(embed=embtd)
        elif server == 'siege':
            embsi = discord.Embed(color = 0x00A725)
            embsi.add_field(name="Статус сервера The Siege", value=f"Игроков: {siege.get_status()['players']}\nКарта: {siege.get_status()['map']}")
            embsi.add_field(name="Сервера", value="```hub, survival, attack, sandbox, pvp, hexed, td, siege```")
            await ctx.send(embed=embsi)
    except:
        servernotwork = discord.Embed()
        servernotwork.add_field(name="Ошибка", value="Сервер офлайн, или его не существует.")
        await ctx.send(embed=servernotwork)
@client.command()
async def eval(ctx, argument):
    embeval = discord.Embed()
    ev = eval(argument)
    embeval.add_field(name="Eval", value=f"{ev}")
    ctx.send(embed=embeval)
    
@client.remove_command("help")

@client.command(pass_context=True)
async def ping(ctx):
        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        ping = round((time_2-time_1)*1000)
        await ctx.send(f"ping = {ping}")

client.run('ODYxNTQxMjg3MTYxMTAyMzc2.YOLS2Q.ehatCiqePEhDB5I06kwJUKlqVLw')
