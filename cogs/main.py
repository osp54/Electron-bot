import nextcord
import json
import datetime
import humanize
from nextcord.ext import commands
from utils.misc import format_name, get_lang, get_prefix
from nextcord.ext.commands import cooldown, BucketType
from configparser import ConfigParser

#print(bundle.get("RU", title))

class main(commands.Cog, name="main"):
    def __init__(self, bot):
        self.bot = bot
        self.b = ConfigParser() # b - bundle
        self.maxcharsprefix = 4
        self.languages = ['ru', 'RU', 'Russian'.lower(), 'en', 'EN', 'English'.lower()]
    @commands.command()
    async def test(self, ctx):
        #bundle = ConfigParser()
        self.b.read(f"locales/{get_lang(self.bot, ctx.message)}.ini")
        await ctx.send(self.b.get('Bundle', 'embed.title',).format(ctx.author, ctx.guild.name))
    @commands.command(
        name = "setprefix",
        usage = "`setprefix [новый префикс]`",
        aliases=['префикс']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix):
        """
        Изменить префикс.
        """
        self.b.read(f"locales/{get_lang(self.bot, ctx.message)}.ini")
        if get_prefix(self.bot, ctx.message) == prefix:
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
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        await ctx.guild.me.edit(nick=f"[{prefix}] Electron Bot")
        eembed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.succerfully'),
            description=self.b.get('Bundle', 'embed.prefixchanged.description').format(get_prefix(self.bot, ctx.message)),
            color=0x42F56C
        ).set_footer(text=self.b.get('Bundle', 'embed.prefix.prompt'))
        await ctx.send(embed=eembed)
    @commands.command(
        name="setlang",
        usage="`setlang [язык]`",
        aliases=['язык', 'lang']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def setlang(self, ctx, lang):
        """
        Изменить язык бота.
        """
        self.b.read(f"locales/{get_lang(self.bot, ctx.message)}.ini")
        if lang not in self.languages:
            eembed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'error.embed.unknownlang.description'),
                color=0xE02B2B
            )
            return await ctx.send(embed=eembed)
        if lang == 'RU'.lower() or lang == 'Russian'.lower():
            lang = 'ru'
        if lang == 'EN'.lower() or lang == 'English'.lower():
            lang = 'en'
        with open("guildlang.json", "r") as f:
            guildlang = json.load(f)
        guildlang[str(ctx.guild.id)] = lang
        with open("guildlang.json", "w") as f:
            json.dump(guildlang, f, indent=4)
        embed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.succerfully'),
            description=self.b.get('Bundle', 'embed.langchanged.description').format(lang),
            color=0x42F56C
        )
        await ctx.send(embed=embed)
    @commands.command(
        name="ping",
        usage="`ping`",
        aliases=['пинг']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ping(self, ctx):
        self.b.read(f"locales/{get_lang(self.bot, ctx.message)}.ini")
        await ctx.send(self.b.get('Bundle', 'ping').format(round(self.bot.latency * 1000)))
    @commands.command(
        name="avatar",
        usage="`avatar <участник>`",
        aliases=['аватар']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def avatar(self, ctx, member: nextcord.Member = None):
        """
        Получить аватар пользователя
        """
        self.b.read(f"locales/{get_lang(self.bot, ctx.message)}.ini")
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
        usage="`emoji [эмодзи]`",
        aliases=["эмодзи_инфо", "эмодзи", "эмоция", "emoteinfo"]
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def emoji(self, ctx, emoji: nextcord.Emoji):
        """
        Эмодзи.
        """
        self.b.read(f"locales/{get_lang(self.bot, ctx.message)}.ini")
        embed = nextcord.Embed(title=self.b.get('Bundle', 'embed.emoji.title'), color=0x42F56C)
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
        usage="`guild`",
        aliases=["guildinfo", "сервер"]
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def guild(self, ctx):
        """Информация об этом сервере."""
        self.b.read(f"locales/{get_lang(self.bot, ctx.message)}.ini")
        guild = ctx.guild
        guild_owner = self.bot.get_user(guild.owner_id)

        features = "\n".join(format_name(f) for f in guild.features)

        embed = nextcord.Embed(title=f"Сервер {guild.name}", color=0x42F56C)
        embed.add_field(name=self.b.get('Bundle', 'embed.guild.name'), value=guild.name)
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
        usage="`channel <канал>`",
        aliases=['канал', 'channelinfo']
    )
    async def channel(self, ctx, channel: nextcord.TextChannel = None):
        """
        Информация о текущем/другом канале.
        """
        self.b.read(f"locales/{get_lang(self.bot, ctx.message)}.ini")
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
       usage="poll [заголовок]",
       aliases=['опрос']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def poll(self, ctx, *, title):
        """
        Создайте опрос, в котором участники могут голосовать.
        """
        self.b.read(f"locales/{get_lang(self.bot, ctx.message)}.ini")
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
