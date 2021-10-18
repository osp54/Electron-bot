import nextcord
from utils.mongo import MongoM

class ConfirmButton(nextcord.ui.View):
    def __init__(self, user):
        super().__init__()
        self.value = None
        self.user = user

    @nextcord.ui.button(emoji='✅', style=nextcord.ButtonStyle.green)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id != self.user.id:
            return await interaction.response.send_message('Ты не автор команды!', ephemeral=True)
        await interaction.response.send_message('Готово.', ephemeral=True)
        self.value = True
        self.stop()

    @nextcord.ui.button(emoji='❌', style=nextcord.ButtonStyle.gray)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id != self.user.id:
            return await interaction.response.send_message('Ты не автор команды!', ephemeral=True)
        await interaction.response.send_message('Отклонено.', ephemeral=True)
        self.value = False
        self.stop()

class SetLangButton(nextcord.ui.View):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.value = None

    @nextcord.ui.button(label="English", style=nextcord.ButtonStyle.green)
    async def english(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = True
        if interaction.user.id != self.user:
            return
        await MongoM().setLang(interaction.guild.id, "en")
        embed = nextcord.Embed(
            title="Successfully",
            description="The language of my messages is set to English",
            color=0x42F56C
        )
        await interaction.edit_original_message(embed=embed)
        self.stop()

    @nextcord.ui.button(label="Русский", style=nextcord.ButtonStyle.gray)
    async def russian(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = True
        if interaction.user.id != self.user:
            return
        await MongoM().setLang(interaction.guild.id, "ru")
        embed = nextcord.Embed(
            title="Успешно!",
            description="Язык моих сообщений установлен на английский",
            color=0x42F56C
        )
        await interaction.edit_original_message(embed=embed)
        self.stop()
