import nextcord

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

class ConfirmButton(nextcord.ui.View):
    def __init__(self, user):
        super().__init__()
        self.value = None
        self.user = user
    @nextcord.ui.button(emoji='❌', style=nextcord.ButtonStyle.green)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id != self.user.id:
            return await interaction.response.send_message('Ты не автор команды!', ephemeral=True)
        await interaction.response.send_message('Готово.', ephemeral=True)
        self.value = True
        self.stop()

    @nextcord.ui.button(emoji='✅', style=nextcord.ButtonStyle.grey)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id != self.user.id:
            return await interaction.response.send_message('Ты не автор команды!', ephemeral=True)
        await interaction.response.send_message('Отклонено.', ephemeral=True)
        self.value = False
        self.stop()

class SetLangButton(nextcord.ui.View):
    def __init__(self, user):
        super().__init__()
        self.value = None
        self.user = user

    @nextcord.ui.button(label="English", style=nextcord.ButtonStyle.green)
    async def english(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id != self.user.id:
            return
        await interaction.response.send_message('The language of my messages has been successfully set to English!')
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Русский", style=nextcord.ButtonStyle.gray)
    async def russian(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id != self.user.id:
            return
        await interaction.response.send_message('Язык моих сообщений успешно установлен на Русский!')
        self.value = False
        self.stop()
