from discord.ext import commands
from discord import Embed
from internal import constants


class Greeting(commands.Cog, name="Greet newcomers."):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        if ctx.channel.id == constants.WELCOME_CHANNEL_ID:
            return True

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = Embed(title=f"Hello, {member.mention}")
        embed.add_field(
            name="Welcome to the IT & CS ACC Students Server!", value="Placeholder"
        )
        await self.bot.get_channel(constants.WELCOME_CHANNEL_ID).send(embed=embed)


def setup(bot):
    """Add Cog to Discord bot."""
    bot.add_cog(Greeting(bot))
