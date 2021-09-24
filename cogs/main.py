import nextcord
import json
import datetime
import humanize
import sqlite3
from nextcord.ext import commands
from utils.Button import SetLangButton
from utils.misc import format_name, get_lang, get_prefix2
from nextcord.ext.commands import cooldown, BucketType
from configparser import ConfigParser

#print(bundle.get("RU", title))

class main(commands.Cog, name="main"):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect(r'db/electron.db')
        self.b = ConfigParser() # b - bundle
        self.maxcharsprefix = 4
    @commands.command(aliases=['префикс'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def setprefix(self, ctx, prefix):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        if get_prefix2(ctx.message) == prefix:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'error.embed.same.prefix.description'),
                color=0xE02B2B
            )
            return await ctx.send(embed=embed)
        if len(prefix) >= self.maxcharsprefix:
            eeembed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'error.embed.max.num.of.chars.in.prefix.description').format(self.maxcharsprefix),
                color=0xE02B2B
            )
            return await ctx.send(embed=eeembed)
        cursor = self.conn.cursor()
        cursor.execute("""SELECT prefix FROM guild WHERE ID = ?""", (ctx.guild.id,))
        result =  cursor.fetchone()
        if result is None:
            cursor.execute("""INSERT INTO guild(ID, prefix) VALUES(?,?)""", (ctx.guild.id, prefix,))
            self.conn.commit()
            eembed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.succerfully'),
                description=self.b.get('Bundle', 'embed.prefixchanged.description').format(prefix),
                color=0x42F56C
            ).set_footer(text=self.b.get('Bundle', 'embed.prefix.prompt'))
            await ctx.send(embed=eembed)
        elif result is not None:
            cursor.execute("""UPDATE guild SET prefix = ? WHERE ID = ?""", (prefix, ctx.guild.id,))
            self.conn.commit()
            eeembed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.succerfully'),
                description=self.b.get('Bundle', 'embed.prefixchanged.description').format(prefix,),
                color=0x42F56C
            ).set_footer(text=self.b.get('Bundle', 'embed.prefix.prompt'))
            await ctx.send(embed=eeembed)
        await ctx.guild.me.edit(nick=f"[{prefix}] Electron Bot")
    @commands.command(
        name="setlang",
        aliases=['язык', 'lang']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def setlang(self, ctx):
        cursor = self.conn.cursor()
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        embed = nextcord.Embed( 
            title=self.b.get('Bundle', 'embed.setlang.title'),
            description=self.b.get('Bundle', 'embed.choose-lang'),
            color=0x42F56C
        )
        view = SetLangButton(ctx.author.id)
        await ctx.send(embed=embed, view=view)
        if view.value:
            cursor.execute("""SELECT lang FROM guild WHERE ID = ?""", (ctx.guild.id,))
            result = cursor.fetchone()
            if result is None:
                cursor.execute("""INSERT INTO guild(ID, lang) VALUES(?,?)""", (ctx.guild.id, "en",))
                self.conn.commit()
            if result is not None:
                cursor.execute("""UPDATE guild SET lang = ? WHERE ID = ?""", ("en", ctx.guild.id,))
                self.conn.commit()
        else:
            cursor.execute("""SELECT lang FROM guild WHERE ID = ?""", (ctx.guild.id,))
            result = cursor.fetchone()
            if result is None:
                cursor.execute("""INSERT INTO guild(ID, lang) VALUES(?,?)""", (ctx.guild.id, "ru",))
                self.conn.commit()
            if result is not None:
                cursor.execute("""UPDATE guild SET lang = ? WHERE ID = ?""", ("ru", ctx.guild.id,))
                self.conn.commit()
    @commands.command(
        name="ping",
        aliases=['пинг']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ping(self, ctx):
        self.b.read(f"locales/{get_lang( ctx.message)}.ini")
        await ctx.send(self.b.get('Bundle', 'ping').format(round(self.bot.latency * 1000)))
    @commands.command(
        name="avatar",
        aliases=['аватар']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def avatar(self, ctx, member: nextcord.Member = None):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        if not member:
            member = ctx.message.author
        embed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.avatar.title').format(member),
            color=0x42F56C
        )
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)
    @commands.command(
        name="emoji",
        aliases=["эмодзи_инфо", "эмодзи", "эмоция", "emoteinfo"]
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def emoji(self, ctx, emoji: nextcord.Emoji):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        embed = nextcord.Embed(title=self.b.get('Bundle', 'embed.emoji.title').format(emoji.name), color=0x42F56C)
        embed.set_thumbnail(url=emoji.url)
        embed.set_image(url=emoji.url)
        embed.add_field(name="ID", value=emoji.id)
        if emoji.user:
            embed.add_field(name=self.b.get('Bundle', 'embed.emoji.who.author.emoji'), value=emoji.user)
        embed.add_field(name=self.b.get('Bundle', 'embed.emoji.server'), value=emoji.guild)
        embed.add_field(
            name=self.b.get('Bundle', 'embed.emoji.whencreated'),
            value=f'{nextcord.utils.format_dt(emoji.created_at, "F")} ({nextcord.utils.format_dt(emoji.created_at, "R")})',
        )
        embed.add_field(name="URL", value=f"[Here]({emoji.url})")
        await ctx.send(embed=embed)
    @commands.command(
        name="guild",
        aliases=["guildinfo", "сервер"]
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def guild(self, ctx):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        guild = ctx.guild
        guild_owner = self.bot.get_user(guild.owner_id)

        features = "\n".join(format_name(f) for f in guild.features)

        embed = nextcord.Embed(title=guild.name, color=0x42F56C)
        embed.add_field(name="ID", value=int(guild.id))
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.owner'), value=guild_owner)
        embed.add_field(name="Icon URL", value=f"[here]({guild.icon.url})")
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.region'), value=str(guild.region))
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.verefication.lvl'), value=str(guild.verification_level))
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.members'), value=len(guild.members))
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.boost.lvl'), value=guild.premium_tier)
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.boosts'), value=guild.premium_subscription_count)
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.boosters'), value=len(guild.premium_subscribers))
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.channels'), value=len(guild.channels))
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.text.channels'), value=len(guild.text_channels))
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.voice.channels'), value=len(guild.voice_channels))
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.categories'), value=len(guild.categories))
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.roles'), value=len(guild.roles))
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.emojis'), value=f"{len(guild.emojis)}/{guild.emoji_limit}")
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.limit.file'), value="{round(guild.filesize_limit / 1048576)} MB")
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.features'), value=features)
        embed.set_thumbnail(url=guild.icon.url)
        await ctx.send(embed=embed)
    @commands.command(
        name="channel",
        aliases=['канал', 'channelinfo']
    )
    async def channel(self, ctx, channel: nextcord.TextChannel = None):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        channel = channel or ctx.channel
        embed = nextcord.Embed(title=self.b.get('Bundle', 'embed.channel').format(channel), color=0x42F56C)
        if channel.topic:
            embed.add_field(name=self.b.get('Bundle', 'embed.channel.desc'), value=channel.topic, inline=False)
        embed.add_field(
            name=self.b.get('Bundle', 'embed.channel.when.created'),
            value=f'{nextcord.utils.format_dt(channel.created_at, "F")}  ({nextcord.utils.format_dt(channel.created_at, "R")})',
        )
        embed.add_field(name="ID", value=channel.id)
        embed.add_field(name=self.b.get('Bundle', 'embed.channel.type'), value=channel.type)
        embed.add_field(name=self.b.get('Bundle', 'embed.channel.position'), value=f"{channel.position}/{len(ctx.guild.text_channels)}")
        embed.add_field(name=self.b.get('Bundle', 'embed.channel.category'), value=channel.category.name)
        if channel.slowmode_delay:
            embed.add_field(
                name=self.b.get('Bundle', 'embed.channel.slowmode.title'),
                value=f"{channel.slowmode_delay} sec ({humanize.naturaldelta(datetime.timedelta(seconds=int(channel.slowmode_delay)))})",
            )
        
        await ctx.send(embed=embed)
    @commands.command(
       name="poll",
       aliases=['опрос']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def poll(self, ctx, *, title):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        embed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.poll.newpoll.title'),
            description=f"{title}",
            color=0x42F56C
        )
        embed.set_footer(
            text=self.b.get('Bundle', 'embed.poll.footer').format(ctx.author)
        )
        embed_message = await ctx.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")
def setup(bot):
    bot.add_cog(main(bot))
