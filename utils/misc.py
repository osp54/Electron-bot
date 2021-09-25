import colorama
import pendulum
import nextcord
import sqlite3
import json
from nextcord.ext.commands import when_mentioned_or
from configparser import ConfigParser
from colorama import init, Fore, Back, Style

conn = sqlite3.connect(r'db/electron.db')
cur = conn.cursor()


#def get_prefix(client, message):
#    with open("prefixes.json", "r") as f:
#        prefixes = json.load(f)
#    return prefixes[str(message.guild.id)]

def get_prefix2(client, message):
    cur.execute("""SELECT prefix FROM guild WHERE ID = ?""", (message.guild.id,))
    result = cur.fetchone()
    if result is not None:
        return result[0]
    else:
        return "$"
def get_lang(message):
    cur.execute("""SELECT lang FROM guild WHERE ID = ?""", (message.guild.id,))
    result = cur.fetchone()
    if result is not None:
       return result[0]
    else:
        return "en"
def localize(ctx, self, to_local, bundle="Bundle"):
    self.b.read(f"locales/{get_lang( ctx.message)}.ini")
    try:
        return self.b.get(bundle, to_local)
    except:
        self.b.read(f"locales/en.ini")
        return self.b.get(bundle, to_local)
def info(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.WHITE}[{now.day}:{now.hour}:{now.minute}:{now.second}] " + Fore.BLUE + f"[I] {Fore.RESET}" + desc)
def error(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.WHITE}[{now.day}:{now.hour}:{now.minute}:{now.second}] " + Fore.RED + f"[E] " + desc)

def format_name(name: str) -> str:
    return name.replace("_", " ").title().strip()
