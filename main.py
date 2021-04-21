from pathlib import Path

import discord
import os
import dotenv
import logging
from pretty_help import PrettyHelp
from discord.ext import commands


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(";"),
    description="A bot for CS/IT @ ACC Discord server.",
    intents=discord.Intents.all(),
    help_command=PrettyHelp(show_index=False, color=discord.Color.purple()),
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


dotenv.load_dotenv(".env")
BOT_TOKEN = os.getenv("BOT_TOKEN")
await bot.start(BOT_TOKEN)
