from discord.ext import commands
from discord import Member, File
from internal import constants
from internal.constants import HOMEWORK_HELP_CHANNEL_ID, WELCOME_CHANNEL_ID
from internal.embed_util import server_embed


class Greeting(commands.Cog, name="Greet newcomers."):
    def __init__(self, bot):
        self.bot = bot
        self.homework_help_channel = self.bot.get_channel(HOMEWORK_HELP_CHANNEL_ID)
        self.welcome_channel = self.bot.get_channel(WELCOME_CHANNEL_ID)

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        # TODO: Add guild ID to constants.py and change to get_guild
        guild = await self.bot.fetch_guild(constants.GUILD_ID)
        embed, file = server_embed(title="Hello!")
        image = File("assets/riverbat.jpg", filename="riverbat.jpg")
        embed.set_image(url="attachment://riverbat.jpg")
        embed.add_field(
            name=f"Welcome to the {guild.name}!",
            value="We hope you enjoy your stay. :grin:",
            inline=False,
        )
        embed.add_field(
            name="Homework Help",
            value=f"Go to {self.homework_help_channel.mention} and ask your question!",
        )

        await self.bot.get_channel(constants.WELCOME_CHANNEL_ID).send(
            f"{member.mention}", embed=embed, files=[file, image]
        )


def setup(bot):
    """Add Cog to Discord bot."""
    bot.add_cog(Greeting(bot))
