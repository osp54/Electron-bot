import nextcord
import traceback
import json
from utils.misc import get_prefix2, info
from nextcord.ext import commands

electron = ['electron', 'электрон']

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mclient = pymongo.MongoClient("mongodb+srv://electron:W$2ov3b$Fff58ludgg@cluster.xyknx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.collg = mclient.electron.guilds
    @commands.Cog.listener('on_message')
    async def on_bot_mention(self, message):
        if '<@861541287161102376>' == message.content:
            prefix = get_prefix2(self.bot, message)
            await message.reply(f"Привет! Мой префикс: `{prefix}`", mention_author=True)
        for i in electron:
            if i in message.content.lower():
                await message.add_reaction("⚡")
    @commands.Cog.listener()
    async def on_command(self, ctx):
        cmd = ctx.command.qualified_name
        info(f"Executed {cmd} command in {ctx.guild.name} (ID: {ctx.message.guild.id}) by {ctx.message.author} (ID: {ctx.message.author.id})")
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
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.MissingPermissions):
            missingperms = ""
            for x in range(len(error.missing_permissions)):
                missingperms += f"`{error.missing_permissions[x]}` "
            missingperms = missingperms.upper()
            return await ctx.send(
                embed = nextcord.Embed(
                    title='Ошибка',
                    description=f'**{ctx.author.name}**, У вас нет прав для использования этой команды.',
                    color=0xFF0000
                ).add_field(name="Необходимые права", value=f"```\n{missingperms}\n```")
            )
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed = nextcord.Embed(title='Ошибка', description=f'У этой команды кулдавн! Пожалуйста подождите {error.retry_after:.2f}s', color=0xFF0000))
        elif isinstance(error, commands.BotMissingPermissions):
            botmissingperms = ""
            for x in range(len(error.missing_permissions)):
                botmissingperms += f"`{error.missing_permissions[x]}` "
            botmissingperms = botmissingperms.upper()
            return await ctx.send(
                embed = nextcord.Embed(
                    title='Ошибка',
                    description=f'У бота нет прав для исполнения этой команды.',
                    color=0xFF0000
                ).add_field(name="Необходимые права", value=f"```\n{botmissingperms}\n```")
            )
        elif isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
            embed = nextcord.Embed(
                title=ctx.command.name.capitalize(),
                color=0xFF0000
            ).add_field(
                name="Использование",
                value=ctx.command.usage
            )
            aliase = '('
            for alias in ctx.command.aliases:
                aliase += f" `{alias}` "
            embed.add_field(
                name="Алиасы(под-имена)",
                value=f"{aliase})"
            )
            return await ctx.send(embed=embed)
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
            if new.content.startswith(get_prefix2(self.bot, new)):
                await self.bot.process_commands(new)
        except:
            return
    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        pass #TODO: Подсчёт вызванных команд.
def setup(bot):
    bot.add_cog(events(bot))
