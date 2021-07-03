import discord
from discord import Embed, File
from internal.constants import ACC_PURPLE


def server_embed(title: str, desc: str = "", url: str = "") -> tuple[Embed, File]:
    embed = discord.Embed(title=title, description=desc, color=ACC_PURPLE, url=url)
    file = File("assets/logo.png", filename="image.png")
    embed.set_author(name="ACC RiverBot")
    embed.set_thumbnail(url="attachment://image.png")
    embed.set_footer(text="Created & maintained by ACC Students.")
    return embed, file
