import nextcord
from utils.bot import get_lang
from configparser import ConfigParser
from nextcord.ext import commands

bot: commands.Bot = ""
b = ConfigParser()

@commands.command(
    name="poll",
    aliases=['опрос']
)
@commands.cooldown(1, 2, commands.BucketType.user)
async def poll(ctx, title, *, args):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    arg = args.split()
    title = title.replace("_", " ")
    counter = 1
    text = ""
    for i in arg:
        text += str(counter) + ". " + i + "\n"
        counter += 1
    embed = nextcord.Embed(
        title=title,
        description=text,
        color=0x42F56C
    )
    embed.set_footer(
        text=b.get('Bundle', 'embed.poll.footer').format(ctx.author)
    )
    embed_message = await ctx.send(embed=embed)
    await embed_message.add_reaction("1️⃣")
    await embed_message.add_reaction("2️⃣")
    await embed_message.add_reaction("3️⃣")
    await embed_message.add_reaction("4️⃣")
    await embed_message.add_reaction("5️⃣")
    await embed_message.add_reaction("6️⃣")
    await embed_message.add_reaction("7️⃣")
    await embed_message.add_reaction("8️⃣")
    await embed_message.add_reaction("9️⃣")

def setup(_bot):
    global bot
    bot = _bot
    return poll