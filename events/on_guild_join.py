import nextcord
from nextcord.ext import commands
from configparser import ConfigParser
from utils import MongoM

b = ConfigParser()
bot: commands.Bot = ""

@commands.Cog.listener()
async def on_guild_join(guild):
    await MongoM().addGuild(guild.id)
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed = nextcord.Embed(
                title="Hey!",
                description="Thanks you for adding me to your server! If your server is in Russian, you can change the language of my messages with the command `$language`, to view other my commands write $help.",
                color=0x006EEF
            )
            await channel.send(embed=embed)
        break

def setup(_bot):
    global bot
    bot = _bot
    return on_guild_join