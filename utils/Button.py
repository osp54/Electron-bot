import nextcord
from utils.mongo import MongoM

class DarkdustryFAQButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @nextcord.ui.button(label="1", style=nextcord.ButtonStyle.green)
    async def f1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title="1. IP серверов",
            description="IP адреса серверов:\n```\n" \
                "Хаб - darkdustry.ml\n" \
                "Атака - darkdustry.ml:1500\n" \
                "Песочница - darkdustry.ml:2000\n" \
                "Выживание - darkdustry.ml:3000\n" \
                "PvP - darkdustry.ml:5000\n" \
                "HexPvP - darkdustry.ml:6000\n" \
                "TowerDefense - darkdustry.ml:7000\n" \
                "Siege - darkdustry.ml:8000\n" \
                "CastleWars - darkdustry.ml:9000\n```\n" \
                "Если вы не знаете, куда вводить IP адрес, спросите об этом в #👋┃помощь, вам помогут.\n" \
                "Так же сервера есть в глобальном списке серверов.\n" \
                "Версия - V7 build 133",
            color=0x3F00FF
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
    @nextcord.ui.button(label="2", style=nextcord.ButtonStyle.green)
    async def f2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title="Как получить разбан?",
            description="Soon",
            color=0x3F00FF
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
class notifyMemberBan(nextcord.ui.View):
     def __init__(self, member):
         super().init()
         self.member = member
     @nextcord.ui.button(label="Да", style=nextcord.ButtonStyle.red)
     async def yes(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
         if Interaction.user.guild_permissions.ban_members:
             await interaction.guild.ban(nextcord.Object(id=self.member.id), reason=interaction.user.name)
             await interaction.message.edit(content=f"{interaction.user.name} забанил вышедшего участника {member.name}")
     @nextcord.ui.button(label="Нет", style=nextcord.ButtonStyle.green)
     async def no(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
         if Interaction.user.guild_permissions.ban_members:
             await interaction.message.edit(content=f"{interaction.user.name} отменил бан вышедшего участника.")
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
