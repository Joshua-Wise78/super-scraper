import discord
from discord.ext import commands
from discord import app_commands

from utils import save_to_json


class General(commands.Cog):
    """
    TODO:
        1. Robust Error handling needs to be put in place to return logs & codes
            to the user for errors.
        2. Add capabilities for multiple directory or files within one function
            call for ease of use.
    Greetings
        Testing method used to test the bot, simply greets user.

    Store_Site
        Store a site to json file for usage later.
        Args:
            site (str): The URL of the site.
            key (str): Name of the site for easy retrievability.

    Retrieve_Site
        Retrieve a site from json to display to the user.
        Args:
            key (str): Key of the site to be retrieved.

    List_Site(s)
        List site(s) for the user to select from.
        Eventually will need a param for filename
    """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="greetings", description="Greet the user")
    async def greet(
        self, interaction: discord.Interaction, user: discord.Member, message: str
    ):
        await interaction.response.send_message(f"Hey {user.mention}! {message}")

    @app_commands.command(name="store_site", description="Store a site")
    async def storeSite(self, interaction: discord.Interaction, key: str, site: str):
        save_to_json(key, site)
        await interaction.response.send_message(f"Saved {site} to {key}")

    @app_commands.command(name="retrieve_site", description="Retrieve Site")
    async def retrieveSite(self, interaction: discord.Interaction, key: str):
        site = []
        await interaction.response.send_message(f"Site: {site}")

    @app_commands.command(name="list_site(s)", description="List sites from storage")
    async def listSites(self, interaction: discord.Interaction):
        sites = []
        await interaction.response.send_message(f"Site: {sites}")


async def setup(bot):
    await bot.add_cog(General(bot))
