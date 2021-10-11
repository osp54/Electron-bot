import motor.motor_asyncio.motor_asyncio

class mongo_Menager():
  def __init__(self):
    self.client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://electron:W$2ov3b$Fff58ludgg@cluster.xyknx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    self.collg = self.client.electron.guilds
  #TODO