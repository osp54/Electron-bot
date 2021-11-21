import nextcord
import json
from configparser import ConfigParser
import inspect
from nextcord.ext import commands
from utils.json import rm_guild_from_BL, add_guild_to_BL
from utils.bot import localize
from utils.console import error, info

class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot
        self.b = ConfigParser()
    @commands.group(aliases=['bl'])
    @commands.is_owner()
    async def blacklist(self, ctx):
        pass
    @blacklist.command()
    @commands.is_owner()
    async def add(self, ctx, gguild: nextcord.Guild):
        with open("blackguilds.json") as file:
            blackguilds = json.load(file)
        if gguild.id in blackguilds['ids']:
            return await ctx.send(f"Сервер {gguild.name} уже в черном списке!")
        await add_guild_to_BL(gguild.id)
        if gguild in self.bot.guilds:
            await gguild.leave()
            for channel in gguild.text_channels:
                if channel.permissions_for(gguild.me).send_messages:
                    await channel.send("This guild blacklisted. Bye!")
                break
        await ctx.send(f"Сервер {gguild.name} добавлен в черный список.")
    @blacklist.command(aliases=['rm'])
    @commands.is_owner()
    async def remove(self, ctx, id: int):
       with open("blackguilds.json") as file:
            blackguilds = json.load(file)
       if guild.id not in blackguilds['ids']:
           return await ctx.send(f"Сервера с id `{id}` нету в черном списке.")
       await rm_guild_from_BL(guild.id)
       await ctx.send("Сервер с id `{id}` удалён из черного списка.")
    @blacklist.command()
    @commands.is_owner()
    async def list(self, ctx):
       with open("blackguilds.json") as file:
            blackguilds = json.load(file)
       text = ""
       for guildId in blackguilds['ids']:
           text = f"{guildId}"
       await ctx.send(text)
    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx):
        messages = []
        for guild in self.bot.guilds:
             messages.append(f"`{guild.name}`: {guild.id}")
        await ctx.send("\n".join(messages))
    @commands.command()
    @commands.is_owner()
    async def geti(self, ctx, id: int):
        guild = self.bot.get_guild(id)
        for channel in guild.text_channels:
            invite = await channel.create_invite()
            break
        try:
            await ctx.author.send(invite)
        except:
            await ctx.send(invite)
    @commands.command()
    @commands.is_owner()
    async def gleave(self, ctx, id: int):
        guild = self.bot.get_guild(id)
        await guild.leave()
        await ctx.send(f"Вышел из гильдии: {guild.name}")
    @commands.command(name='embed')
    @commands.is_owner()
    async def embed(self, ctx,*, message):
        await ctx.message.delete()
        embed=nextcord.Embed(description=message, color=0xFF0000)
        await ctx.send(embed=embed)
    @commands.command(name='say')
    @commands.is_owner()
    async def say(self, ctx,*, message):
        if ctx.message.reference is not None:
            ref_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            await ref_msg.reply(message)
        else:
            await ctx.send(message)
    @commands.command()
    @commands.is_owner()
    async def ttest(self, ctx):
        await ctx.send(localize(ctx, self, "test.test"))
def setup(bot):
    bot.add_cog(owner(bot))
