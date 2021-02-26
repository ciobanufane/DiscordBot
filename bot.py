import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')
TEST_CHANNEL = os.getenv('TEST_CHANNEL_TOKEN')

bot = commands.Bot(command_prefix="!")

@bot.command(name='echo')
async def echo(ctx, *args):
    test_channel = discord.utils.get( bot.get_all_channels(),name=TEST_CHANNEL)
    await ctx.send(" ".join(args))

@bot.command(name='test')
async def test(ctx):
    await ctx.send("test")

@bot.command(name="ntc")
async def new_text_channel(ctx):
    pass

@bot.command(name="nvc")
async def new_voice_channel(ctx):
    pass

@bot.command(name="new_role")
async def create_role(ctx):
    pass


bot.run(TOKEN)