import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

class help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot
    @commands.group(name="help", aliases=['хелп', 'помощь'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def help(self, ctx):
        """
        Список всех команд
        """
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title="Help", description=f"Префикс: {ctx.prefix}", color=0x42F56C)
            cogs = ("Main", "Moderation", "Music")
            for i in cogs:
                cog = self.bot.get_cog(i.lower())
                commands = cog.get_commands()
                command_list = [command.name for command in commands]
                command_description = [command.help for command in commands]
                help_text = '\n'.join(f'{n} - {h}' for n, h in zip(command_list, command_description))
                embed.add_field(name=i.capitalize(), value=f'```\n{help_text}\n```', inline=False)
                embed.set_footer(text='ElectronBot.tk | Все права защищены')
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar.url)
            await ctx.send(embed=embed)
    @help.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def main(self, ctx):
       embed = discord.Embed(title="Help", description=f"Префикс: {ctx.prefix}", color=0x42F56C)
       cog = self.bot.get_cog("main")
       commands = cog.get_commands()
       command_list = [command.name for command in commands]
       command_description = [command.help for command in commands]
       help_text = '\n'.join(f'{n} - {h}' for n, h in zip(command_list, command_description))
       embed.add_field(name='Main', value=f'```\n{help_text}\n```', inline=False)
       embed.set_footer(text='ElectronBot.tk | Все права защищены')
       embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar.url)
       await ctx.send(embed=embed)
    @help.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def moderation(self, ctx):
       embed = discord.Embed(title="Help", description=f"Префикс: {ctx.prefix}", color=0x42F56C)
       cog = self.bot.get_cog("moderation")
       commands = cog.get_commands()
       command_list = [command.name for command in commands]
       command_description = [command.help for command in commands]
       help_text = '\n'.join(f'{n} - {h}' for n, h in zip(command_list, command_description))
       embed.add_field(name=Moderation, value=f'```\n{help_text}\n```', inline=False)
       embed.set_footer(text='ElectronBot.tk | Все права защищены')
       embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar.url)
       await ctx.send(embed=embed)
    @help.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def music(self, ctx):
       embed = discord.Embed(title="Help", description=f"Префикс: {context.prefix}", color=0x42F56C)
       cog = self.bot.get_cog("music")
       commands = cog.get_commands()
       command_list = [command.name for command in commands]
       command_description = [command.help for command in commands]
       help_text = '\n'.join(f'{n} - {h}' for n, h in zip(command_list, command_description))
       embed.add_field(name='Music', value=f'```\n{help_text}\n```', inline=False)
       embed.set_footer(text='ElectronBot.tk | Все права защищены')
       embed.set_author(name=context.message.author, icon_url=context.message.author.avatar.url)
       await context.send(embed=embed)
def setup(bot):
    bot.add_cog(help(bot))
