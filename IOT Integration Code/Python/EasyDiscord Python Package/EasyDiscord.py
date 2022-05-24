from discord.ext import commands

from dotenv import dotenv_values, load_dotenv

load_dotenv(".env", verbose=True)


_secrets = dotenv_values(".env", verbose=True)

#intents = discord.Intents.all()
#intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"))


@bot.command()
async def test(ctx, *args):
    ctx.send(f"__test__: \n{args}")


@bot.command()
async def load(ctx, module: str):
    bot.load_extension(module)


@bot.command()
async def reload(ctx, module: str):
    bot.reload_extension(module)


@bot.command()
async def raw_test(ctx):
    print("raw_test called!")
    await ctx.send("__test__ test command")

bot.run(_secrets["DISCORD_BOT_TOKEN"])
