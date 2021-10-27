import colorama
import os
import nextcord
import json
from datetime import datetime
from configparser import ConfigParser
from colorama import init, Fore, Back, Style

cp = ConfigParser()

def format_name(name: str) -> str:
    return name.replace("_", " ").title().strip()
