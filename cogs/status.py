import nextcord as discord
import threading
import os
import psutil
from utils.mongo import MongoM
from datetime import datetime
from nextcord.ext import commands, tasks

tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=30)
    async def status(self):
        now = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
        channel = self.bot.get_channel(881924597472178176)
        msg = await channel.fetch_message(881924714073845760)
        embed = discord.Embed(
            title = "Статистика",
            description = f"Статистика нагрузки на хостинг бота.\nПоследнее обновление статуса: `{now}` Moscow",
            color = 0x00A725
        )
        embed.add_field( name = "Выполненные команды", value = await MongoM().getExecutedCmds())
        embed.add_field( name = "CPU", value = f"Нагрузка на процессор: {psutil.cpu_percent()}%", inline = False)
        embed.add_field( name = "RAM", value = f"ОЗУ: {used_m}/{tot_m}MB", inline = True)
        embed.add_field( name = "Потоки", value = threading.active_count(), inline = False)
        await msg.edit(embed = embed)

    @commands.Cog.listener()
    async def on_ready(self):
        self.status.start()
def setup(bot):
    bot.add_cog(status(bot))
