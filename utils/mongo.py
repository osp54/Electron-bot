import motor.motor_asyncio

class MongoM():
    def __init__(self, coll = "guilds"):
        self.client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://electron:W$2ov3b$Fff58ludgg@cluster.xyknx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.coll = self.client.electron[coll]
    async def connect(self):
        try:
            await self.client.admin.command('ismaster')
            #info("Succerfully connected to database.")
        except Exception as e:
            pass
            #error(f"Failed connect to database. Error: {e}")
    async def setPrefix(self, guild_id, prefix: str):
        self.coll = self.client.electron.guilds
        return await self.coll.update_one({"_id": guild_id}, {"$set": {"prefix": prefix}})
    async def setLang(self, guild_id, lang: str):
        self.coll = self.client.electron.guilds
        return await self.coll.update_one({"_id": guild_id}, {"$set": {"lang": lang}})
    async def setMuteRole(self, guild_id, role_id):
        self.coll = self.client.electron.guilds
        return await self.coll.update_one({"_id": guild_id}, {"$set": {'mute_role': role_id}})
    async def getMuteRole(self, guild_id):
        self.coll = self.client.electron.guilds
        res = await self.coll.find_one({"_id": guild_id})
        try:
            return res["mute_role"]
        except:
            return
    async def addGuild(self, guild_id: int):
        self.coll = self.client.electron.guilds
        if await self.coll.count_documents({"_id": guild_id}) == 0:
            res = await self.coll.insert_one({"_id": guild_id, "lang": "en", "prefix": "$"})
            #info(f"Added guild with ID {guild_id} to database.")
            return res
    async def getPrefix(self, guild_id: int):
        self.coll = self.client.electron.guilds
        res = await self.coll.find_one({"_id": guild_id})
        return res["prefix"]
    async def getLang(self, guild_id: int):
        self.coll = self.client.electron.guilds
        res = await self.coll.find_one({"_id": guild_id})
        return res["lang"]