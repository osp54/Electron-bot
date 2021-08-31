import nextcord
import json
from functions import get_prefix
from nextcord.ext import commands

electron = ['Electron', 'electron', 'ELECTRON', 'Электрон', 'электрон', 'ЭЛЕКТРОН']

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        if '<@861541287161102376>' == message.content:
            prefix = get_prefix(self.bot, message)
            await message.reply(f"Привет! Мой префикс: `{prefix}`", mention_author=True)
        for i in electron:
            if i in message.content:
                await message.add_reaction("⚡")
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("prefixes.json", "r", encoding="UTF-8") as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = "$"
        with open("prefixes.json", "w", encoding="UTF-8") as f:
            json.dump(prefixes, f, indent=4)

        with open("guildlang.json", "r", encoding="UTF-8") as f:
            guildlang = json.load(f)

        guildlang[str(guild.id)] = "English"
        with open("guildlang.json", "w") as f:
            json.dump(guildlang, f, indent=4)

        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                embed = nextcord.Embed(
                    title="Hey!",
                    description="Thanks you for adding me to your server! If your server is in Russian, you can change the language of my messages with the command `$setlang Russian`, to view other my commands write $help.",
                    color=0x006EEF
                ).add_field(
                    name="Features",
                    value="Auto remove scam links like 'free nitro'! Music! And much more.")
                await ctx.send(embed=embed)
            break
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("prefixes.json", "r", encoding="UTF-8") as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))
        with open("prefixes.json", "w", encoding="UTF-8") as f:
            json.dump(prefixes, f, indent=4)

        with open("guildlang.json", "r", encoding="UTF-8") as f:
            guildlang = json.load(f)

        guildlang.pop(str(guild.id))
        with open("guildlang.json", "w", encoding="UTF-8") as f:
            json.dump(prefixes, f, indent=4)
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
                title=ctx.command.name.upper(),
                color=0xFF0000
            ).add_field(
                name="Использование",
                value=ctx.command.usage
            )
            aliase = '( '
            for alias in ctx.command.aliases:
                aliase += alias + " "
            embed.add_field(
                name="Алиасы(под-имена)",
                value=f"{aliase})"
            )
            return await ctx.send(embed=embed)
        else:
           channel = self.bot.get_channel(872078345137979434)
           error = getattr(error, 'original', error)
           if hasattr(ctx.command, 'on_error'):
                return

           if ctx.cog:
               if ctx.cog._get_overridden_method(ctx.cog.cog_command_error) is not None:
                   return
           embed = nextcord.Embed(
               title="New Error",
               description=f"Command: {ctx.command.name}\n\nUsername: `{ctx.author}`\n\nUserID: `{ctx.author.id}`\n\nGuild Name: `{ctx.guild.name}`",
               color=0x42F56C
           )
           embed.add_field(
                   name="Error:",
                   value=f"```\n{ctx.author} - {error}\n```"
           )
           await channel.send(embed=embed)
    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        pass #TODO: Подсчёт вызванных команд.
def setup(bot):
    bot.add_cog(events(bot))
