from nextcord.ext import commands

bot: commands.Bot = ""

@commands.command(name='say')
@commands.is_owner()
async def say(ctx, *, message):
    if ctx.message.reference is not None:
        ref_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        try:
            await ctx.message.delete()
        except:
            pass
        return await ref_msg.reply(message)
    try:
        await ctx.message.delete()
    except:
        pass
    await ctx.send(message)

def setup(_bot):
    global bot
    bot = _bot
    return say