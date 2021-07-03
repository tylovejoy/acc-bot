from discord.ext import commands
from discord import Embed
from discord.utils import escape_markdown
from internal.embed_util import server_embed


class Quotes(commands.Cog, name="Quotes"):
    """Quotes"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        help="Quickly display specific quotes.",
        brief="Quickly display specific quotes.",
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
        help='Displays the link for "Don\'t ask to ask, just ask!"',
        brief='Displays the link for "Don\'t ask to ask, just ask!"',
        aliases=["dontask"],
    )
    async def dataja(self, ctx):
        await ctx.send("https://dontasktoask.com/")

    @tag.command(
        help="How to properly format code on Discord!",
        brief="How to properly format code on Discord!",
        aliases=["format", "code"],
    )
    async def formatcode(self, ctx):
        embed, file = server_embed(
            title="Code Formatting",
            desc="Please format your code for Discord. It makes it so much easier to read.\nㅤ\n",
        )
        embed.add_field(
            name="Python Code",
            value=(
                escape_markdown('```py\nprint("Hello")\n```')
                + "\nWill look like this:\n"
                '```py\nprint("Hello")\n```\nㅤ\n'
            ),
            inline=False,
        )
        embed.add_field(
            name="C++ Code",
            value=(
                escape_markdown('```c++\ncout << "Hello, World!" << endl;\n```')
                + "\nWill look like this:\n"
                '```c++\ncout << "Hello, World!" << endl;\n```\nㅤ\n'
            ),
            inline=False,
        )
        embed.add_field(
            name="Many other languages work!",
            value="Click this link for a complete list: https://highlightjs.org/static/demo/\nㅤ\n",
            inline=False,
        )
        await ctx.send(embed=embed, file=file)


def setup(bot):
    """Add Cog to Discord bot."""
    bot.add_cog(Quotes(bot))
