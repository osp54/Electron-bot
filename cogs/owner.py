import nextcord
import json
from nextcord.ext import commands
from utils.json import rm_guild_from_BL, add_guild_to_BL
from utils.misc import error, info, Confirm
class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='load')
    @commands.is_owner()
    async def load(self, ctx, dir, cog):
        try:
            self.bot.load_extension(f"{dir[2:]}.{cog}")
            info(f"Loaded extension {cog}")
            await ctx.send("Готово!")
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            error(f"Failed to load extension {cog}\n{exception}")
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
        add_guild_to_BL(gguild.id)
        for guild in self.bot.guilds:
            if guild.id in blackguilds['ids']:
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).send_messages:
                        await channel.send("This guild is blacklisted. Bye!")
                break
        await ctx.send(f"Сервер {gguild.name} добавлен в черный список.")
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
    async def say(self, ctx,*, message=None):
        await ctx.message.delete()
        await ctx.send(message)
    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        view = Confirm(ctx.message.author)
        await ctx.send('Точно?!', view=view)
        await view.wait()
        if view.value:
            info(f'{ctx.message.author} off the bot!')
            await exit()
def setup(bot):
    bot.add_cog(owner(bot))
