from nextcord.ext import commands

bot: commands.Bot = ""

@commands.command()
@commands.is_owner()
async def gleave(ctx, id: int):
    guild = bot.get_guild(id)
    await guild.leave()
    await ctx.send(f"Вышел из гильдии: {guild.name}")

def setup(_bot):
    global bot
    bot = _bot
    return gleave