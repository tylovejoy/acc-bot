import logging
import os
from pathlib import Path

import discord
import dotenv
from discord.ext import commands
from pretty_help import PrettyHelp

from internal import constants
from internal.constants import ACC_PURPLE

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(";"),
    description="A bot for CS/IT @ ACC Discord server.",
    intents=discord.Intents.all(),
    help_command=PrettyHelp(show_index=False, color=ACC_PURPLE),
    case_insensitive=True,
)


async def load_all_extensions():
    """Load all *.py files in /cogs/ as Cogs."""
    cogs = [x.stem for x in Path("cogs").glob("*.py")]
    logging.info("Loading extensions...\n")
    for extension in cogs:
        try:
            bot.load_extension(f"cogs.{extension}")
            logging.info(f"loaded {extension}")
        except Exception as e:
            error = f"{extension}\n {type(e).__name__} : {e}"
            logging.info(f"failed to load extension {error}")


@bot.event
async def on_ready():
    await load_all_extensions()
    app_info = await bot.application_info()
    logging.info(constants.ACC_ASCII_LOGO)
    logging.info(
        f"\n\nLogged in as: {bot.user.name}\n"
        f"Using discord.py version: {discord.__version__}\n"
        f"Owner: {app_info.owner}\n\n"
    )


@bot.event
async def on_message(message):
    """Allow bot to ignore all other bots."""
    if message.author.bot:
        return
    await bot.process_commands(message)


if __name__ == "__main__":
    dotenv.load_dotenv(".env")
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    logging.basicConfig(level=logging.INFO)
    bot.run(BOT_TOKEN)
