from nextcord.ext import commands

bot: commands.Bot = ""

@commands.command()
@commands.is_owner()
async def geti(ctx, id: int):
    guild = bot.get_guild(id)
    for channel in guild.text_channels:
        invite = await channel.create_invite()
        break
    try:
        await ctx.author.send(invite)
    except:
        await ctx.send(invite)

def setup(_bot):
    global bot
    bot = _bot
    return geti