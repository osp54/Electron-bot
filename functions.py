import colorama
import pendulum
from colorama import init, Fore, Back, Style

def info(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.BLUE}[{Fore.RESET}{now.day}:{now.hour}:{now.minute}:{now.second}{Fore.BLUE}] " + Fore.BLUE + f"[I] {Fore.RESET}" + desc)
def error(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.RED}[{Fore.RESET}{now.day}:{now.hour}:{now.minute}:{now.second}{Fore.RED}] " + Fore.RED + f"[E] " + desc)
