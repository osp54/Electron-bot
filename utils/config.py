from configparser import ConfigParser

config = ConfigParser()

def get(name: str, section: str = "Bot"):
    config.read("./config.ini")
    return config.get(section, name)