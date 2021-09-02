import nextcord
import discordSuperUtils
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType
from discordSuperUtils import MusicManager, PageManager


class music(commands.Cog, name="music"):
    def __init__(self, bot):
            self.client_id = 861541287161102376
            self.client_secret = 'FR8vHPfRkhnHPQpyIdXO_QN1yX80tB04'
            self.bot = bot

            self.MusicManager = MusicManager(self.bot, client_id=self.client_id, client_secret=self.client_secret)
            self.MusicManager.add_event(self.on_music_error, 'on_music_error')
            self.MusicManager.add_event(self.on_play, 'on_play')

    async def on_music_error(self, ctx, error):
        pass

    async def on_play(self, ctx, player):
        await ctx.send(f"Играет `{player}`\n{player.data['webpage_url']}")

    @commands.command(aliases=['выйти'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def leave(self, ctx):
        """
        Выйти из голосового канала.
        """
        if await self.MusicManager.leave(ctx):
            await ctx.send("Вышел из голосового канала.")
            await ctx.message.add_reaction('✅')

    @commands.command(
        name="play",
        usage="`play [название песни/ссылка]`",
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def play(self, ctx, *, query: str):
        """
        Проиграть песню.
        """
        voice = nextcord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await self.MusicManager.join(ctx)
        player = await self.MusicManager.create_player(query)
        if player:
            await self.MusicManager.queue_add(player=player, ctx=ctx)
            await ctx.message.add_reaction('✅')
            if not await self.MusicManager.play(ctx):
                await ctx.send(f"Добавлено в очередь")
                await ctx.message.add_reaction('✅')
        else:
            await ctx.send("Запрос не найден.")

    @commands.command(
        name="skip",
        usage="skip",
        aliases=['скип']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def skip(self, ctx, index: int = None):
        """
        Пропустить текущую песню.
        """
        await self.MusicManager.skip(ctx, index)
        await ctx.message.add_reaction('✅')

    @commands.command(
        name="np",
        usage="`np`",
        aliases=['сейчас_играет', 'now_playing']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def np(self, ctx):
        """
        Сейчас играет.
        """
        await ctx.send(f"Сейчас играет: `{await self.MusicManager.now_playing(ctx)}`")

    @commands.command(
        name="volume",
        usage="`volume [частота звука]`",
        aliases=['громкость']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def volume(self, ctx, volume: int):
        """
        Сделать больше/меньше громкость звука
        """
        await self.MusicManager.volume(ctx, volume)
        await ctx.message.add_reaction('✅')

    @commands.command(
        name="loop",
        usage="`loop`",
        aliases=['зациклить']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def loop(self, ctx):
        """
        Зациклить текущую песню.
        """
        is_loop = await self.MusicManager.loop(ctx)
        await ctx.send(f"Looping toggled to `{is_loop}`")
        await ctx.message.add_reaction('✅')
    @commands.command(
        name="queueloop",
        usage="`queueloop`",
        aliases=['цикл_очередь']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def queueloop(self, ctx):
        """
        Зациклить текущую очередь.
        """
        is_loop = await self.MusicManager.queueloop(ctx)
        await ctx.send(f"Queue looping toggled to `{is_loop}`")
        await ctx.message.add_reaction('✅')
    @commands.command(
        name="history",
        usage="`history`",
        aliases=['история']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def history(self, ctx):
        """
        История проигравших песен.
        """
        embeds = discordSuperUtils.generate_embeds(await self.MusicManager.history(ctx),
                                                   "Song History",
                                                   "Shows all played songs",
                                                   25,
                                                   string_format="Title: `{}`")

        page_manager = PageManager(ctx, embeds, public=True)
        await page_manager.run()

    @commands.command(
        name="queue",
        usage="`queue`",
        aliases=['очередь']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def queue(self, ctx):
        """
        Очередь песен.
        """
        embeds = discordSuperUtils.generate_embeds(await self.MusicManager.get_queue(ctx),
                                                   "Очередь",
                                                   f"Сейчас играет: `{await self.MusicManager.now_playing(ctx)}`",
                                                   25,
                                                   string_format="Title: {}")
        page_manager = PageManager(ctx, embeds, public=True)
        await page_manager.run()
def setup(bot):
    bot.add_cog(music(bot))
