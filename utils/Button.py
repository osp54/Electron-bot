import nextcord
from utils.mongo import MongoM

class notifyMemberBan(nextcord.ui.View):
     def __init__(self, member):
         super().__init__(timeout=None)
         self.member = member
     @nextcord.ui.button(label="Да", style=nextcord.ButtonStyle.red)
     async def yes(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
         if interaction.user.guild_permissions.ban_members:
             await interaction.guild.ban(nextcord.Object(id=self.member.id), reason=interaction.user.name)
             await interaction.message.edit(content=f"{interaction.user} забанил вышедшего участника {self.member}.")
             button.disabled = True
             self.stop()
     @nextcord.ui.button(label="Нет", style=nextcord.ButtonStyle.green)
     async def no(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
         if interaction.user.guild_permissions.ban_members:
             await interaction.message.edit(content=f"{interaction.user} отменил бан вышедшего участника {self.member}.")
             button.disabled = True
             self.stop()
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
        await interaction.message.edit(embed=embed)
        self.clear_items()
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
        await interaction.message.edit(embed=embed)
        self.clear_items()
        self.stop()
