from datetime import datetime
from colorama import Fore

def info(desc):
    now = datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    print(f"{Fore.WHITE}[{now}] " + Fore.BLUE + f"[I] {Fore.RESET}" + desc)
def error(desc):
    now = datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    print(f"{Fore.WHITE}[{now}] " + Fore.RED + f"[E] " + desc)
