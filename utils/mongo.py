import motor.motor_asyncio
from utils.misc import info, error

class MongoM():
  def __init__(self, coll = "guilds"):
    self.client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://electron:W$2ov3b$Fff58ludgg@cluster.xyknx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    self.coll = self.client.electron[coll]
  async def connect(self):
    try:
      await self.admin.command('ismaster')
      info("Succerfully connected to database.")
    except Exception as e:
      error("Failed to connect to database. Error: {e}")
  async def setPrefix(self, ctx, prefix: str):
    self.coll = self.client.electron.guilds
    return await self.coll.update_one({"_id": ctx.guild.id}, {"$set": {"prefix": prefix}})
  async def setLang(self, ctx, lang: str):
    self.coll = self.client.electron.guilds
    return await self.coll.update_one({"_id": ctx.guild.id}, {"$set": {"lang": lang}})
  async def addGuild(self, guild_id: int):
    self.coll = self.client.electron.guilds
    return await self.coll.insert_one({"_id": guild_id, "lang": "en", "prefix": "$"})
  async def getPrefix(self, guild_id: int):
    self.coll = self.client.electron.guilds
    res = await self.coll.find_one({"_id": guild_id})
    return res["prefix"]
  async def getLang(self, guild_id: int):
    self.coll = self.client.electron.guilds
    res = await self.coll.find_one({"_id": guild_id})
    return res["lang"]
  
    