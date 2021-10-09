import nextcord
from utils.misc import info, error, unload_extensions
from nextcord.ext import commands
args = {
        "nextcord": nextcord,
        "sauce": getsource,
        "sys": sys,
        "os": os,
        "imp": __import__,
        "this": self,
        "ctx": ctx
}
class commandline(commands.Cog, name="commandline"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.is_owner()
    async def start_console(self, ctx):
        await ctx.message.add_reaction("✅")
        info("Console commands has started")
        while True:
            conl = input()
            if conl.startswith("eval"):
                code = prepare(conl.replace("eval ", "").format("\n"))
                try:
                    exec(f"async def func():{code}", args)
                    a = time()
                    response = await eval("func()", args)
                    print(f"{self.resolve_variable(response)}{type(response).__name__} | {(time() - a) / 1000} ms`")
                except Exception as e:
                    error(e)
            elif conl.startswith("exit"):
                unload_extensions(self.bot, "./cogs")
                await self.bot.close()
            else:
                error("Command not found")
def setup(bot):
    bot.add_cog(commandline(bot))
