import nextcord
from configparser import ConfigParser
from utils.mongo import MongoM
from utils.bot import get_lang
from nextcord.ext import commands

scam_links = ["steamcommunity.link", "discorcl.link", "steamcommunity.com.ru", "steamcommunnity.ru", "steamccommunity.com.ru", "steamcommuunity.com.ru", "surl.li", "stearncornmrunity.ru.com", "fustcup.ru", "steamcommrunity.com", "brapo.space", "steamcommunutiy.com", "discord.giveawey.com"]
bad_words = ["free nitro", "бесплатное нитро", "nitro free", "нитро бесплатно", "раздача бесплатного нитро", "раздача нитро", "нитро раздача", "нитро раздача бесплатно", "nitro distribution", "distribution nitro"]
discord_domains = ["com", "gg"]

class anti_scam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.b = ConfigParser()
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild is None:
            return
        if not await MongoM().checkAntiScam(message.guild.id):
            return
        self.b.read(f"locales/{await get_lang(message)}.ini")
        for word in bad_words:
            if word in message.content.lower():
                return await message.reply(f"WARNING! Scam detected! Ban this member or give punishment! Member: {message.author}, id: {message.author.id}")
        msg = message.content.split()
        for m in msg:
            for d in discord_domains:
                if m.startswith("disc") and not m.endswith(d):
                     embed = nextcord.Embed(
                        title=self.b.get('Bundle', 'embed.warning'),
                        description=self.b.get('Bundle', 'embed.antiscam.warning.desc').format(message.author, message.author.id),
                        color=0xE02B2B
                     )
                     return await message.reply(embed=embed)
                     #return await message.reply(f"WARNING! Scam detected! Ban this member or give punishment! Member: {message.author}, id: {message.author.id}")
        for link in scam_links:
            if link in message.content.lower():
                try:
                    await message.delete()
                    embed = nextcord.Embed(
                        title=self.b.get('Bundle', 'embed.warning'),
                        description=self.b.get('Bundle', 'embed.antiscam.warning.desc').format(message.author, message.author.id),
                        color=0xE02B2B
                    )
                    return await message.channel.send(embed=embed)
                except:
                    embed = nextcord.Embed(
                        title=self.b.get('Bundle', 'embed.warning'),
                        description=self.b.get('Bundle', 'embed.antiscam.warning.desc').format(message.author, message.author.id),
                        color=0xE02B2B
                    )
                    return await message.reply(embed=embed)
                    #return await message.reply(f"WARNING! Scam link detected! Ban this member or give punishment! Member: {message.author}, id: {message.author.id}")

def setup(bot):
    bot.add_cog(anti_scam(bot))
