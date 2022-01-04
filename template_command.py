from nextcord.ext import commands

bot: commands.Bot = ""

@commands.command()
async def command(ctx):
    pass

def setup(_bot):
    global bot
    bot = _bot
    return command