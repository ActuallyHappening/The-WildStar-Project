import json
import logging
import discord
from discord.ext import commands
import AIO

from dotenv import dotenv_values, load_dotenv

load_dotenv(".env", verbose=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


_secrets = dotenv_values(".env", verbose=True)

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("$"), intents=intents)


@bot.command()
async def test(ctx, *args):
    ctx.send(f"__test__: \n{args}")


@bot.command()
async def load(ctx, module: str):
    bot.load_extension(module)


@bot.command()
async def reload(ctx, module: str):
    bot.reload_extension(module)


@bot.event
async def on_message(message):
    logger.debug(f"{message=}")
    logger.debug(f"{message.content=}")

    if message.content == "delete_channel":
        print("Deleting channel ...")
        await message.channel.delete(reason="Deleted through command")

    if message.content == "delete_channels pls":
        print("Deleting channels ...")
        for channel in bot.get_all_channels():
            if input(f"Delete {channel.name}? (y/n) ") == "y":
                await channel.delete(reason="Deleted through command")
        # await message.channel.delete(reason="Deleted through command")

    if message.author == bot.user:
        logger.debug(f"{message.author=} RECURSIVE")
        return

    message.content = message.content.replace('\\"', '"')
    try:
        data = json.loads(message.content)
    except json.JSONDecodeError as exc:
        logger.debug("Message not json :)")
        logger.debug(exc)
        logger.debug(f"{message.content}")
        return
        # raise exc
    payload = data["payload"]
    logger.debug(f"{payload=}")
    _project, _action, _input = payload["Project"], payload["Action"], payload["Input"]
    passOn(_project, _action, _input, ctx=message.channel)


def passOn(project, action, _input, *, ctx=None):
    print(f"{project=}")
    print(f"{action=}")
    print(f"{_input=}")
    data = {"__meta__": {"from": "discord"}, "payload": {
        "Project": project, "Action": action, "Input": _input}}
    AIO.send("embedded", "embedded-to-test", data=json.dumps(data))


'''
@bot.command()
async def delete_channel(ctx, channel: discord.TextChannel):
'''


@bot.command()
async def raw_test(ctx):
    print("raw_test called!")
    await ctx.send("__test__ test command")

bot.run(_secrets["DISCORD_BOT_TOKEN"])
