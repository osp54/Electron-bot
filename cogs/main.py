import discord
import os
import sys
import json
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

class main(commands.Cog, name="main"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['префикс'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix):
        """
        Изменить префикс.
        """
        if ctx.prefix == prefix:
            embed = discord.Embed(
                title="Ошибка",
                description="У этого сервера уже установлен такой префикс!",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            return
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        await ctx.guild.me.edit(nick=f"[{prefix}] Electron Bot")
        await ctx.send(f"Prefix changed to: {prefix}")
    @commands.command(aliases=['язык'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def setlang(self, ctx, lang):
        """
        Изменить язык бота.
        """
        with open("guildlang.json", "r") as f:
            guildlang = json.load(f)
        guildlang[str(ctx.guild.id)] = lang
        with open("guildlang.json", "w") as f:
            json.dump(guildlang, f, indent=4)
        await ctx.send(f"Prefix changed to: {lang}")
    @commands.command(name="avatar", aliases=['аватар'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def avatar(self, ctx, member: discord.Member = None):
        """
        Получить аватар пользователя
        """
        if not member:
            member = ctx.message.author
        embed = discord.Embed(
            title=f"Аватар пользователя {member}",
            color=0x42F56C
        )
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def emoji(self, ctx, emoji: discord.Emoji = None)
        """
        Получить изображение эмодзи.
        """
        if not emoji:
            embed = discord.Embed(
                title="Ошибка",
                description="Введите эмодзи!",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            return
        eembed = discord.Embed(
            title=f"Эмодзи {emoji.name}",
            color=0x42F56C
        )
        eembed.set_image(url=emoji.url)
        await ctx.send(embed=eembed)
    @commands.command(name="poll", aliases=['опрос'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def poll(self, ctx, *, title):
        """
        Создайте опрос, в котором участники могут голосовать.
        """
        embed = discord.Embed(
            title="Создан новый опрос!",
            description=f"{title}",
            color=0x42F56C
        )
        embed.set_footer(
            text=f"Опрос создан: {ctx.message.author} • Жми на реакции!"
        )
        embed_message = await ctx.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")
def setup(bot):
    bot.add_cog(main(bot))
