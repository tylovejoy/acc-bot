from discord.ext import commands
from discord import Embed

from internal.embed_util import server_embed


class Quotes(commands.Cog, name="Quotes"):
    """Quotes"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        help="",
        brief="",
        aliases=["quote"],
    )
    async def tag(self, ctx):
        if ctx.invoked_subcommand is None:
            embed, file = server_embed(
                title="Quick quotes!",
                desc="Here's a list of quotes you can use.",
            )
            for cmd in self.bot.get_command("tag").walk_commands():

                embed.add_field(
                    name=f"{cmd} [{', '.join(cmd.aliases)}]",
                    value=f"{cmd.help}",
                    inline=False,
                )
            await ctx.send(embed=embed, file=file)

    @tag.command(
        help="Don't ask to ask, just ask!",
        brief="",
        aliases=["dontask"],
    )
    async def dataja(self, ctx):
        await ctx.send("https://dontasktoask.com/")


def setup(bot):
    """Add Cog to Discord bot."""
    bot.add_cog(Quotes(bot))
