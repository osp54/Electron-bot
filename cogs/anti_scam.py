import nextcord
from nextcord.ext import commands

scam_links = ["steamcommunity.link", "discorcl.link", "steamcommunity.com.ru", "steamcommunnity.ru", "steamccommunity.com.ru", "steamcommuunity.com.ru", "surl.li", "stearncornmrunity.ru.com", "fustcup.ru", "steamcommrunity.com", "brapo.space", "steamcommunutiy.com", "discord.giveawey.com"]
bad_words = ["free nitro", "бесплатное нитро", "nitro free", "нитро бесплатно", "раздача бесплатного нитро", "раздача нитро", "нитро раздача", "нитро раздача бесплатно", "nitro distribution", "distribution nitro"]
bad_domains = [".ru.com", ".link", ".gift"]

class anti_scam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        for word in bad_words:
            if word in message.content.lower() and "https://" in message.content.lower() or "http://" in message.content.lower():
                return await message.reply(f"WARNING! Scam detected! Ban this member or give punishment! Member: {message.author}, id: {message.author.id}")
        msg = message.content.split()
        for m in msg:
            for d in bad_domains:
                if m.startswith("https://disc") or m.startswith("http://disc") and m.endswith(d):
                     return await message.reply(f"WARNING! Scam detected! Ban this member or give punishment! Member: {message.author}, id: {message.author.id}")
        for link in scam_links:
            if link in message.content.lower():
                try:
                    await message.delete()
                    return await ctx.send(f"I deleted the post with the scam link. I recommend banning or punishing this member. Member: {message.author}, id: {message.author.id}")
                except:
                    return await message.reply(f"WARNING! Scam link detected! Ban this member or give punishment! Member: {message.author}, id: {message.author.id}")
  
def setup(bot):
    bot.add_cog(anti_scam(bot))
