import motor.motor_asyncio
import sys
from utils import config
from utils.log import error, info

class MongoM():
    def __init__(self, coll = "guilds"):
        try:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(config.get("mongodb-con-string"))
            self.coll = self.client["electron"][coll]
            self.connect()
        except Exception as e:
            error(f"Connect to database failed. Error: {e}")
            sys.exit()
    async def connect(self):
        try:
            await self.client.admin.command('ismaster')
            info("Succerfully connected to database.")
        except Exception as e:
            error(f"Failed connect to database. Error: {e}")
    async def setPrefix(self, guild_id, prefix: str):
        return await self.coll.update_one({"_id": guild_id}, {"$set": {"prefix": prefix}})
    async def setLang(self, guild_id, lang: str):
        self.coll = self.client.electron.guilds
        return await self.coll.update_one({"_id": guild_id}, {"$set": {"lang": lang}})
    async def setMuteRole(self, guild_id, role_id):
        return await self.coll.update_one({"_id": guild_id}, {"$set": {'mute_role': role_id}})
    async def getMuteRole(self, guild_id):
        res = await self.coll.find_one({"_id": guild_id})
        try:
            return res["mute_role"]
        except KeyError or TypeError:
            return
    async def addGuild(self, guild_id: int):
        if await self.coll.count_documents({"_id": guild_id}) == 0:
            res = await self.coll.insert_one({"_id": guild_id, "lang": "en", "prefix": "$"})
            info(f"Added guild with ID {guild_id} to database.")
            return res
    async def getPrefix(self, guild_id: int):
        res = await self.coll.find_one({"_id": guild_id})
        return res["prefix"]
    async def getLang(self, guild_id: int):
        res = await self.coll.find_one({"_id": guild_id})
        return res["lang"]
    async def setAntiScam(self, guild_id: int, value: bool):
        return await self.coll.update_one({"_id": guild_id}, {"$set": {"anti_scam": value}})
    async def checkAntiScam(self, guild_id: int):
        res = await self.coll.find_one({"_id": guild_id})
        try:
            return bool(res["anti_scam"])
        except KeyError or TypeError:
            return False
    async def getExecutedCmds(self):
        res = await self.coll.find_one({"_id": 872078273553764372})
        return res["executed_cmds"]