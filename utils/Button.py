import nextcord
from utils.mongo import MongoM

class DarkdustryFAQButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    @nextcord.ui.button(label="1", style=nextcord.ButtonStyle.green)
    async def f1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title="1",
            description="хз",
            color=0x3F00FF
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
    @nextcord.ui.button(label="2", style=nextcord.ButtonStyle.green)
    async def f2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title="2",
            description="хзхз",
            color=0x3F00FF
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
class SetLangButton(nextcord.ui.View):
    def __init__(self, user):
        super().__init__()
        self.user = user

    @nextcord.ui.button(label="English", style=nextcord.ButtonStyle.green)
    async def english(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id != self.user:
            return
        await MongoM().setLang(interaction.guild.id, "en")
        embed = nextcord.Embed(
            title="Successfully",
            description="The language of my messages is set to English",
            color=0x42F56C
        )
        self.clear_items()
        await interaction.message.edit(embed=embed)
        self.stop()

    @nextcord.ui.button(label="Русский", style=nextcord.ButtonStyle.gray)
    async def russian(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id != self.user:
            return
        await MongoM().setLang(interaction.guild.id, "ru")
        embed = nextcord.Embed(
            title="Успешно!",
            description="Язык моих сообщений установлен на русский",
            color=0x42F56C
        )
        self.clear_items()
        await interaction.message.edit(embed=embed)
        self.stop()
