import json


async def add_guild_to_BL(user_id: int):
    with open("blackguilds.json", "r+") as file:
        file_data = json.load(file)
        file_data["ids"].append(user_id)
    with open("blackguilds.json", "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)


async def rm_guild_from_BL(user_id: int):
    with open("blackguilds.json", "r") as file:
        file_data = json.load(file)
        file_data["ids"].remove(user_id)
    with open("blackguilds.json", "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)
