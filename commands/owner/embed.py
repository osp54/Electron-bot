import nextcord
from nextcord.ext import commands

bot: commands.Bot = ""

@commands.command(name='embed')
@commands.is_owner()
async def embed(ctx, *, message):
    await ctx.message.delete()
    embed = nextcord.Embed(description=message, color=0xFF0000)
    await ctx.send(embed=embed)

def setup(_bot):
    global bot
    bot = _bot
    return embed