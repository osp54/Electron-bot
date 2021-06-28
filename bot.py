import discord
import socket
import psutil
import asyncio
import os
import random
import time
from config import settings
from discord.ext import tasks,commands
from datetime import datetime

client = discord.Client()

tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

client = commands.Bot(command_prefix = settings['prefix'])

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name=f"CPU = {psutil.cpu_percent()}%"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name=f"CPU = {psutil.cpu_percent()}%"))
        await asyncio.sleep(10)

@client.command()
async def status(ctx):
   await ctx.send("status")

@client.event
async def on_ready():
    sping.start()
    client.loop.create_task(status_task())

async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        emb2 = discord.Embed( title = "Yes!", description = "Приветствуем тебя на нашем сервере {member.mention}!\nРекомендуем прочитать правила.", color = 0x00A725)
        embed.set_footer(text=f"Теперь нас {ctx.guild.member_count}!")
        await guild.system_channel.send(embed=emb2)

@tasks.loop(seconds=settings['updateSts'])
async def sping():
    def isOpen(ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return True
        except:
            return False
    server_siege = isOpen("35.202.253.94", 6567)
    server_comm = isOpen("35.202.253.94", 0000)
    channel = client.get_channel(settings['channelid'])
    msg = await channel.fetch_message(settings['msgid'])
    emb = discord.Embed( title = "Status", description = f"Статус обновляется каждые 15 секунд.\nПоследнее обновление статуса: \n{datetime.now()}", color = 0x00A725)
    if server_siege: 
        emb.add_field( name = "The Siege", value = "35.202.253.94  :green_circle: ", inline = False)
    else:
        emb.add_field( name = "The Siege", value = "35.202.253.94  :red_circle: ", inline = False)
    if server_comm:
        emb.add_field( name = "Soon", value = "35.202.253.94:7776   :green_circle: ", inline = False)
    else:
        emb.add_field( name = "Soon", value = "35.202.253.94:7776   :red_circle: ", inline = False)
    emb.add_field( name = "CPU", value = f"CPU Usage = {psutil.cpu_percent()}% ", inline = False)
    emb.add_field( name = "RAM", value = f"RAM Usage = {used_m}MB/{tot_m}MB", inline = True)
    await msg.edit(embed = emb)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Напишите больше подробностей...')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("У тебя нет прав на эту команду.")
    if isinstance(error, commands.CommandNotFound ):
        emb4 = discord.Embed( title = "Ошибка...", description = f" команда не найдена!", color = 0xF0000)
        await ctx.send(embed = emb4)
@client.remove_command("help")
@client.command()
async def help(ctx):
        emb3 = discord.Embed( title = "Help", description = "Список всех комманд", color = 0x00A725)
        emb3.add_field( name = "Moderation", value ="```.ban``` <usr.mention> <reason> - забанить пользователя.\n```.unban``` <usr.id> - разбанить пользователя.", inline = False)
        emb3.add_field( name = "Other", value =f"```.ping``` - показать задержку бота.\n\n\nПрефикс бота = {settings['prefix']}", inline = False)
        await ctx.send(embed=emb3)

@client.command(pass_context=True)
async def ping(ctx):
        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        ping = round((time_2-time_1)*1000)
        await ctx.send(f"ping = {ping}")

#The below code bans player.
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#The below code unbans player.
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

client.run(settings['token'])
