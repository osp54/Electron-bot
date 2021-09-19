import colorama
import pendulum
import nextcord
import sqlite3
import json
from configparser import ConfigParser
from colorama import init, Fore, Back, Style

conn = sqlite3.connect(r'db/electron.db')
cur = conn.cursor()


#def get_prefix(client, message):
#    with open("prefixes.json", "r") as f:
#        prefixes = json.load(f)
#    return prefixes[str(message.guild.id)]

def get_prefix2(client, message):
    cur.execute(f"SELECT prefix FROM guild WHERE ID = {message.guild.id}")
    result = cur.fetchone()
    if result is not None:
        return result[0]
    else:
        return "$"
def get_lang(client, message):
    cur.execute(f"SELECT lang FROM guild WHERE ID = {message.guild.id}")
    result = cur.fetchone()
    if result is None:
        return "en"
    if result is not None:
        return result[0]
def info(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.WHITE}[{now.day}:{now.hour}:{now.minute}:{now.second}] " + Fore.BLUE + f"[I] {Fore.RESET}" + desc)
def error(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.WHITE}[{now.day}:{now.hour}:{now.minute}:{now.second}] " + Fore.RED + f"[E] " + desc)

def format_name(name: str) -> str:
    return name.replace("_", " ").title().strip()
