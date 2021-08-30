import nextcord as discord
from nextcord.ext import commands, tasks
import psutil
import os
import time

tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=30)
    def sping(self):
        channel = self.bot.get_channel(881924597472178176)
        msg = await channel.fetch_message(881924714073845760)
        emb = discord.Embed(
            title = "Статистика",
            description = f"Статистика нагрузки на хостинг бота.\nПоследнее обновление статуса: ",
            color = 0x00A725
        )
        emb.add_field( name = "CPU", value = f"Нагрузка на процессор: {psutil.cpu_percent()}% ", inline = False)
        emb.add_field( name = "RAM", value = f"ОЗУ: {used_m}MB/{tot_m}MB", inline = True)
        await msg.edit(embed = emb)

    @commands.Cog.listener()
    async def on_ready(self):
        sping()

def setup(bot):
    bot.add_cog(status(bot))