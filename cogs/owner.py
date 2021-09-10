import nextcord
from nextcord.ext import commands
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
    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx):
        messages = []
        for guild in self.bot.guilds:
             messages.append(f"{guild.name}")
        await ctx.send("\n".join(messages))

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
