import discord
import discordSuperUtils
from discord.ext import commands
from discordSuperUtils import MusicManager, PageManager


class Music(commands.Cog, name="Music"):
    def __init__(self, bot):
            self.client_id = 861541287161102376
            self.client_secret = 'FR8vHPfRkhnHPQpyIdXO_QN1yX80tB04'
            self.bot = bot

            self.MusicManager = MusicManager(self.bot, client_id=self.client_id, client_secret=self.client_secret)

    @self.MusicManager.event()
    async def on_music_error(self, ctx, error):
        pass

    @self.MusicManager.event()
    async def on_play(self, ctx, player):
        await ctx.send(f"Играет {player}")

    @commands.command()
    async def leave(self, ctx):
        if await self.MusicManager.leave(ctx):
            await ctx.send("Вышел из голосового канала.")


    @commands.command()
    async def np(self, ctx):
        if player == await self.MusicManager.now_playing(ctx):
            await ctx.send(f"Сейчас играет: {player}")


    @commands.command()
    async def join(self, ctx):
        if await self.MusicManager.join(ctx):
            await ctx.send("Присоединился к голосовому каналу.")


    @commands.command()
    async def play(self, ctx, *, query: str):
        async with ctx.typing():
            player = await self.MusicManager.create_player(query)
        if player:
            await self.MusicManager.queue_add(player=player, ctx=ctx)

            if not await self.MusicManager.play(ctx):
                await ctx.send("Добавлено в очередь")
        else:
            await ctx.send("Запрос не найден.")

    @commands.command()
    async def volume(self, ctx, volume: int):
        await self.MusicManager.volume(ctx, volume)


    @commands.command()
    async def loop(self, ctx):
        is_loop = await self.MusicManager.loop(ctx)
        await ctx.send(f"Looping toggled to {is_loop}")


    @commands.command()
    async def queueloop(self, ctx):
        is_loop = await self.MusicManager.queueloop(ctx)
        await ctx.send(f"Queue looping toggled to {is_loop}")

    @commands.command()
    async def history(self, ctx):
        embeds = discordSuperUtils.generate_embeds(await MusicManager.history(self, ctx),
                                                   "Song History",
                                                   "Shows all played songs",
                                                   25,
                                                   string_format="Title: {}")

        page_manager = PageManager(self, ctx, embeds, public=True)
        await page_manager.run()

    @commands.command()
    async def skip(self, ctx, index: int = None):
        await self.MusicManager.skip(ctx, index)
        ctx.send("Пропущено...")

    @commands.command()
    async def queue(self, ctx):
        embeds = discordSuperUtils.generate_embeds(await MusicManager.get_queue(self, ctx),
                                                   "Очередь",
                                                   f"Сейчас играет: {await MusicManager.now_playing(ctx)}",
                                                   25,
                                                   string_format="Title: {}")
        page_manager = PageManager(self, ctx, embeds, public=True)
        await page_manager.run()
def setup(bot):
    bot.add_cog(Music(bot))
