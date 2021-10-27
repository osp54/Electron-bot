import nextcord
import traceback
import json
from utils.mongo import MongoM
from configparser import ConfigParser
from utils.bot import get_prefix, get_lang
from utils.console import info, error
from nextcord.ext import commands

electron = ['electron', 'электрон']

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.b = ConfigParser()
    @commands.Cog.listener('on_message')
    async def on_bot_mention(self, message):
        self.b.read(f"locales/{await get_lang(message)}.ini")
        if '<@861541287161102376>' == message.content:
            prefix = await get_prefix(self.bot, message, True)
            await message.reply(self.b.get('Bundle', 'HelloMessage').format(prefix), mention_author=True)
        for i in electron:
            if i in message.content.lower():
                await message.add_reaction("⚡")
    @commands.Cog.listener()
    async def on_command(self, ctx):
        await MongoM().coll.update_one({"_id": 872078273553764372}, {"$inc": {"executed_cmds": 1}})
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("blackguilds.json") as file:
            blackguilds = json.load(file)
        if guild.id in blackguilds["ids"]:
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages:
                    cchannel = channel
                break
            await cchannel.send("This guild is blacklisted. Bye!")
            return await guild.leave()
        await MongoM().addGuild(guild.id)
        await self.bot.change_presence(activity=nextcord.Game(name=f"$help | Guilds: {len(self.bot.guilds)}"))
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                embed = nextcord.Embed(
                    title="Hey!",
                    description="Thanks you for adding me to your server! If your server is in Russian, you can change the language of my messages with the command `$language`, to view other my commands write $help.",
                    color=0x006EEF
                ).add_field(
                    name="Features",
                    value="Auto remove scam links like 'free nitro'! And much more.")
                await channel.send(embed=embed)
            break
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await self.bot.change_presence(activity=nextcord.Game(name=f"$help | Guilds: {len(self.bot.guilds)}"))
    @commands.Cog.listener()
    async def on_message_edit(self, old, new):
        try:
            if new.content.startswith(await get_prefix(self.bot, new)):
                await self.bot.process_commands(new)
        except:
            return
def setup(bot):
    bot.add_cog(events(bot))
