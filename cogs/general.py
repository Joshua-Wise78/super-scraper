import discord
from discord.ext import commands
from discord import app_commands

from utils import save_to_json

class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @app_commands.command(name="greetings", description="Greet the user")
  async def greet(self, interaction: discord.Interaction,
                   user: discord.Member, message: str):
    await interaction.response.send_message(f"Hey {user.mention}! {message}")

  @app_commands.command(name="store_site", description="Store a site")
  async def storeSite(self, interaction: discord.Interaction, key: str, site: str):
    save_to_json(key, site)
    await interaction.response.send_message(f"Saved {site} to {key}")
       
async def setup(bot):
  await bot.add_cog(General(bot))
