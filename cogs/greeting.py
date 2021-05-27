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
        # embed.add_field(
        #     name="Role selection",
        #     value="React with the roles you want access to!",
        #     inline=False,
        # )
        # embed.add_field(name="🔌", value="IT Support", inline=True)
        # embed.add_field(name="⌨", value="Programming", inline=True)
        # embed.add_field(name="🔒", value="Cyber-Security", inline=True)
        # embed.add_field(name="💻", value="Web Development", inline=True)
        await self.bot.get_channel(constants.WELCOME_CHANNEL_ID).send(
            f"{member.mention}",
            embed=embed,
        )
        # await msg.add_reaction("🔌")
        # await msg.add_reaction("⌨")
        # await msg.add_reaction("🔒")
        # await msg.add_reaction("💻")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        pass


def setup(bot):
    """Add Cog to Discord bot."""
    bot.add_cog(Greeting(bot))
