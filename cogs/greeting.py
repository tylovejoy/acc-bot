from discord.ext import commands

from internal import constants


class Greeting(commands.Cog, name="Greet newcomers."):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        if ctx.channel.id == constants.WELCOME_CHANNEL_ID:
            return True

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # TODO: add Embed() to display greeting to user.
        pass


def setup(bot):
    """Add Cog to Discord bot."""
    bot.add_cog(Greeting(bot))
