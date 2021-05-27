from discord.ext import commands
from discord import Embed
from internal import constants


class Greeting(commands.Cog, name="Greet newcomers."):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = Embed(title="Hello!")
        embed.add_field(
            name="Welcome to the IT & CS ACC Students Server",
            value="We hope you enjoy your stay. :)",
            inline=False,
        )
        await self.bot.get_channel(constants.WELCOME_CHANNEL_ID).send(
            f"{member.mention}",
            embed=embed,
        )

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        pass


def setup(bot):
    """Add Cog to Discord bot."""
    bot.add_cog(Greeting(bot))
