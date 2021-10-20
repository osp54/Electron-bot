import nextcord
import traceback
import json
from utils.mongo import MongoM
from configparser import ConfigParser
from utils.misc import get_prefix2, info, cmdInfo, get_lang
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
            prefix = await get_prefix2(self.bot, message, True)
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
    async def on_command_error(self, ctx, error):
        self.b.read(f"locales/{await get_lang(ctx.message)}.ini")
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.NotOwner):
            return
        elif isinstance(error, commands.MissingPermissions):
            missingperms = ""
            for x in range(len(error.missing_permissions)):
                missingperms += f"`{error.missing_permissions[x]}` "
            missingperms = missingperms.upper()
            return await ctx.send(
                embed = nextcord.Embed(
                    title=self.b.get('Bundle', 'embed.error'),
                    description=self.b.get('Bundle', 'embed.error.missing-perms').format(ctx.author),
                    color=0xFF0000
                ).add_field(name=self.b.get('Bundle', 'embed.required-rights'), value=f"```\n{missingperms}\n```")
            )
        elif isinstance(error, commands.CommandOnCooldown):
            return await ctx.send(embed=nextcord.Embed(title=self.b.get('Bundle', 'embed.error'), description=self.b.get('Bundle', 'embed.error.command-in-cooldown').format(error.retry_after), color=0xFF0000))
        elif isinstance(error, commands.BotMissingPermissions):
            botmissingperms = ""
            for x in range(len(error.missing_permissions)):
                botmissingperms += f"`{error.missing_permissions[x]}` "
            botmissingperms = botmissingperms.upper()
            return await ctx.send(
                embed = nextcord.Embed(
                    title=self.b.get('Bundle', 'embed.error'),
                    description=self.b.get('Bundle', 'embed.error.bot-missing-perms'),
                    color=0xFF0000
                ).add_field(name=self.b.get('Bundle', 'embed.required-rights'), value=f"```\n{botmissingperms}\n```")
            )
        elif isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
            await cmdInfo(ctx, self, ctx.command.name)
        else:
           channel = self.bot.get_channel(872078345137979434)
           if hasattr(ctx.command, 'on_error'):
                return
           if ctx.cog:
               if ctx.cog._get_overridden_method(ctx.cog.cog_command_error) is not None:
                   return
           _error = ''.join(traceback.format_exception(type(error), error, error.__traceback__))
           eembed = nextcord.Embed(
               title="Новая ошибка",
               description=_error,
               color=0xFF0000
           )
           __error = getattr(error, 'original', error)
           eembed.add_field(name="Более короткая ошибка", value=__error)
           await channel.send(embed=eembed)
    @commands.Cog.listener()
    async def on_message_edit(self, old, new):
        try:
            if new.content.startswith(await get_prefix2(self.bot, new)):
                await self.bot.process_commands(new)
        except:
            return
def setup(bot):
    bot.add_cog(events(bot))
