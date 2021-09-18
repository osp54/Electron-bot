import colorama
import pendulum
import nextcord
import sqlite3
import json
from configparser import ConfigParser
from colorama import init, Fore, Back, Style

conn = sqlite3.connect(r'db/electron.db')
cur = conn.cursor()


def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
def get_prefix2(client, message):
    cur.execute(f"SELECT prefix FROM guilds WHERE ID = {message.guild.id}")
    result = cur.fetchone()
    if result is None:
        return "$"
    if result is not None:
        return result
def get_lang(client, message):
    with open("guildlang.json", "r") as f:
        guildlang = json.load(f)
    return guildlang[str(message.guild.id)]

def info(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.WHITE}[{now.day}:{now.hour}:{now.minute}:{now.second}] " + Fore.BLUE + f"[I] {Fore.RESET}" + desc)
def error(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.WHITE}[{now.day}:{now.hour}:{now.minute}:{now.second}] " + Fore.RED + f"[E] " + desc)

def format_name(name: str) -> str:
    return name.replace("_", " ").title().strip()

class Confirm(nextcord.ui.View):
    def __init__(self, user):
        super().__init__()
        self.value = None
        self.user = user

    @nextcord.ui.button(emoji='✅', style=nextcord.ButtonStyle.green)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id != self.user.id:
            return await interaction.response.send_message('Ты не автор команды!', ephemeral=True)
        await interaction.response.send_message('Готово.', ephemeral=True)
        self.value = True
        self.stop()

    @nextcord.ui.button(emoji='❌', style=nextcord.ButtonStyle.gray)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id != self.user.id:
            return await interaction.response.send_message('Ты не автор команды!', ephemeral=True)
        await interaction.response.send_message('Отклонено.', ephemeral=True)
        self.value = False
        self.stop()
