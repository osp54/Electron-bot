import discord
import discordSuperUtils
from discord.ext import commands
from discordSuperUtils import MusicManager, PageManager

class Music(commands.Cog, name="Music"):
    def __init__(self, bot):
        self.bot = bot
    client_id = 861541287161102376
    client_secret = FR8vHPfRkhnHPQpyIdXO_QN1yX80tB04
    MusicManager = MusicManager(bot, client_id=client_id, client_secret=client_secret)

    @MusicManager.event()
    async def on_music_error(ctx, error):
        pass

    @MusicManager.event()
    async def on_play(ctx, player):
        await ctx.send(f"Играет {player}")

    @commands.command()
    async def leave(self, ctx):
        if await MusicManager.leave(ctx):
            await ctx.send("Вышел из голосового канала.")


    @commands.command()
    async def np(self, ctx):
        if player == await MusicManager.now_playing(ctx):
            await ctx.send(f"Сейчас играет: {player}")


    @commands.command()
    async def join(self, ctx):
        if await MusicManager.join(ctx):
            await ctx.send("Присоединился к голосовому каналу.")


    @commands.command()
    async def play(self, ctx, *, query: str):
        player = await MusicManager.create_player(query)
        if player:
            await MusicManager.queue_add(player=player, ctx=ctx)

            if not await MusicManager.play(ctx):
                await ctx.send("Добавлено в очередь")
        else:
            await ctx.send("Запрос не найден.")

    @commands.command()
    async def volume(self, ctx, volume: int):
        await MusicManager.volume(ctx, volume)


    @commands.command()
    async def loop(self, ctx):
        is_loop = await MusicManager.loop(ctx)
        await ctx.send(f"Looping toggled to {is_loop}")


    @commands.command()
    async def queueloop(self, ctx):
        is_loop = await MusicManager.queueloop(ctx)
        await ctx.send(f"Queue looping toggled to {is_loop}")

    @commands.command()
    async def history(self, ctx):
        embeds = discordSuperUtils.generate_embeds(await MusicManager.history(ctx),
                                                   "Song History",
                                                   "Shows all played songs",
                                                   25,
                                                   string_format="Title: {}")

        page_manager = PageManager(ctx, embeds, public=True)
        await page_manager.run() 

    @commands.command()
    async def skip(self, ctx, index: int = None):
        await MusicManager.skip(ctx, index)
        ctx.send("Пропущено...")

    @commands.command()
    async def queue(self, ctx):
        embeds = discordSuperUtils.generate_embeds(await MusicManager.get_queue(ctx),
                                                   "Очередь",
                                                   f"Сейчас играет: {await MusicManager.now_playing(ctx)}",
                                                   25,
                                                   string_format="Title: {}")
        page_manager = PageManager(ctx, embeds, public=True)
        await page_manager.run()
def setup(bot):
    bot.add_cog(Music(bot))
