import discord
import socket
import psutil
import ram
from config import settings
from discord.ext import tasks,commands
from datetime import datetime
client = discord.Client()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
client = commands.Bot(command_prefix = settings['prefix'])
@client.command()
async def status(ctx):
   await ctx.send("status")
@client.event
async def on_ready():
    ping.start()
@tasks.loop(seconds=settings['updateSts'])
async def ping():
    def isOpen(ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return True
        except:
            return False
    server_mobile = isOpen("35.202.253.94", 7777)
    server_pc = isOpen("35.202.253.94", 7776)
    channel = client.get_channel(856167446195863583)
    msg = await channel.fetch_message(856174885292998657)
    emb = discord.Embed( title = "Status")
    emb.add_field( name = "CPU", value = f"CPU Usage = {psutil.cpu_percent()}% ", inline = False)
    emb.add_field( name = "RAM", value = f"RAM Usage = {mem_T}MB/{mem_U}MB", inline = True)
    emb.add_field( name = "Servers", value = f"‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍Статус обновляется каждые 15 секунд.\nПоследнее обновление статуса: \n{datetime.now()}", inline = False)
    if server_mobile: 
        emb.add_field( name = "Mobile", value = "35.202.253.94:7777    :green_circle: ", inline = False)
    else:
        emb.add_field( name = "Mobile", value = "35.202.253.94:7777    :red_circle: ", inline = False)
        print(f"{bcolors.OKBLUE}{datetime.now()} {bcolors.OKGREEN}| {bcolors.WARNING}{bcolors.BOLD}[Status Servers] {bcolors.OKBLUE} Server Mobile(35.202.253.94:7777) has down!")
    if server_pc:
        emb.add_field( name = "PC", value = "35.202.253.94:7776   :green_circle: ", inline = False)
    else:
        emb.add_field( name = "PC", value = "35.202.253.94:7776   :red_circle: ", inline = False)
        print(f"{bcolors.OKBLUE}{datetime.now()} {bcolors.OKGREEN}| {bcolors.WARNING}{bcolors.BOLD}[Status Servers] {bcolors.OKBLUE}Server PC(35.202.253.94:7776)has down!")
    await msg.edit(embed = emb)

client.run(settings['token'])
