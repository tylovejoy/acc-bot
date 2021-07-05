from discord import File, Member
from discord.ext import commands

from internal.constants import GUILD_ID, HOMEWORK_HELP_CHANNEL_ID, WELCOME_CHANNEL_ID
from internal.embed_util import server_embed


class Events(commands.Cog, name="Events"):
    """Events"""

    def __init__(self, bot):
        self.bot = bot
        self._cd = commands.CooldownMapping.from_cooldown(
            1.0, 60.0, commands.BucketType.user
        )
        self.homework_help_channel = self.bot.get_channel(HOMEWORK_HELP_CHANNEL_ID)
        self.welcome_channel = self.bot.get_channel(WELCOME_CHANNEL_ID)

    @commands.Cog.listener()
    async def on_message(self, message):
        if "riverbot" in message.content.lower():
            bucket = self._cd.get_bucket(message)
            retry_after = bucket.update_rate_limit()
            if not retry_after:
                await message.channel.send("🦇🦇_\\*Bat screeches\\*_🦇🦇")

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        guild = self.bot.get_guild(GUILD_ID)
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

        await self.welcome_channel.send(
            f"{member.mention}", embed=embed, files=[file, image]
        )


def setup(bot):
    """Add Cog to Discord bot."""
    bot.add_cog(Events(bot))
