import logging
import os
from pathlib import Path

import discord
import dotenv
from discord.ext import commands
from pretty_help import PrettyHelp

from internal import constants
from internal.constants import ACC_PURPLE

logger = logging.getLogger()
logger.setLevel(logging.INFO)

consoleHandle = logging.StreamHandler()
consoleHandle.setLevel(logging.INFO)
consoleHandle.setFormatter(
    logging.Formatter("%(asctime)s :: %(name)-18s :: %(levelname)-8s :: %(message)s")
)
logger.addHandler(consoleHandle)

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
    logger.info("")
    logger.info("Loading extensions...")
    for extension in cogs:
        try:
            bot.load_extension(f"cogs.{extension}")
            logger.info(f"loaded {extension}")
        except Exception as e:
            error = f"{extension} - {type(e).__name__} : {e}"
            logger.warning(error)


@bot.event
async def on_ready():
    await load_all_extensions()
    app_info = await bot.application_info()
    logger.info(constants.ACC_ASCII_LOGO)
    logger.info(
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
    bot.run(BOT_TOKEN)
