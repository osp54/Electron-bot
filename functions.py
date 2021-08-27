import colorama
import pendulum
import json
from colorama import init, Fore, Back, Style
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]
def info(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.BLUE}[{Fore.RESET}{now.day}:{now.hour}:{now.minute}:{now.second}{Fore.BLUE}] " + Fore.BLUE + f"[I] {Fore.RESET}" + desc)
def error(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.RED}[{Fore.RESET}{now.day}:{now.hour}:{now.minute}:{now.second}{Fore.RED}] " + Fore.RED + f"[E] " + desc)

def format_name(name: str) -> str:
    return name.replace("_", " ").title().strip()