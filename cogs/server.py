import discord
from discord.ext import commands
from discord import app_commands

class Server(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="test", description="Testing command")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello!")

async def setup(bot):
    await bot.add_cog(Server(bot))
