from discord.ext import commands
import Adafruit_IO as AIO
from dotenv import dotenv_values, load_dotenv

load_dotenv(".env", verbose=True)

_secrets = dotenv_values(".env", verbose=True)

aio = AIO.Client(_secrets["ADAFRUIT_IO_USERNAME"], _secrets["ADAFRUIT_IO_KEY"])


def send(group: str, feed: str, *, data):
    fullName = group + "." + feed
    aio.send(fullName, data)


@commands.command()
async def AIOsend(ctx, group: str, feed: str, *, data):
    fullName = group + "." + feed
    await ctx.send(f"**Sending in {fullName=}**:\n{data=}")
    aio.send(fullName, data)


@commands.command()
async def AIOreceive(ctx, group: str, feed: str):
    fullName = group + "." + feed
    await ctx.send(f"**Received from {fullName=}:** \n{aio.send(fullName)}")


def setup(bot):
    bot.add_command(AIOsend)
    bot.add_command(AIOreceive)
