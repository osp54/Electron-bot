import nextcord
import traceback
from utils.bot import get_prefix, cmdInfo, get_lang
from nextcord.ext import commands
from configparser import ConfigParser

b = ConfigParser()
bot: commands.Bot = ""


@commands.Cog.listener()
async def on_command_error(ctx, error):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
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
            embed=nextcord.Embed(
                title=b.get('Bundle', 'embed.error'),
                description=b.get('Bundle', 'embed.error.missing-perms').format(ctx.author),
                color=0xFF0000
            ).add_field(name=b.get('Bundle', 'embed.required-rights'), value=f"```\n{missingperms}\n```")
        )
    elif isinstance(error, commands.CommandOnCooldown):
        return await ctx.send(embed=nextcord.Embed(title=b.get('Bundle', 'embed.error'),
                                                   description=b.get('Bundle',
                                                                          'embed.error.command-in-cooldown').format(
                                                       error.retry_after), color=0xFF0000))
    elif isinstance(error, commands.BotMissingPermissions):
        botmissingperms = ""
        for x in range(len(error.missing_permissions)):
            botmissingperms += f"`{error.missing_permissions[x]}` "
        botmissingperms = botmissingperms.upper()
        return await ctx.send(
            embed=nextcord.Embed(
                title=b.get('Bundle', 'embed.error'),
                description=b.get('Bundle', 'embed.error.bot-missing-perms'),
                color=0xFF0000
            ).add_field(name=b.get('Bundle', 'embed.required-rights'), value=f"```\n{botmissingperms}\n```")
        )
    elif isinstance(error, commands.BadArgument) or isinstance(error, commands.MissingRequiredArgument):
        await cmdInfo(ctx, bot, ctx.command.name)
    else:
        channel = bot.get_channel(872078345137979434)
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

def setup(_bot):
    global bot
    bot = _bot
    return on_command_error