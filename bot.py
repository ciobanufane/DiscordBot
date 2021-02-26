import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')
TEST = os.getenv('TEST_CHANNEL_TOKEN')

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print('I am ready')


@bot.command(name='echo')
async def echo(ctx, *args):
    if str(ctx.channel.id) == TEST:
        await ctx.send(" ".join(args), delete_after=15)


@bot.command(name="ntc")
@commands.has_guild_permissions(manage_channels=True)
async def new_text_channel(ctx, channel_name, category_name="Text Channels"):
    exist_cat = discord.utils.get(ctx.guild.categories, name=category_name)
    if not exist_cat:
        await ctx.send(f"No specified category for the text channel")
        return

    exist_channel = discord.utils.get(exist_cat.text_channels, name=channel_name)
    if exist_channel:
        await ctx.send(f"{channel_name} already exists; enter another channel name")
        return

    await ctx.guild.create_text_channel(channel_name, category=exist_cat)


@bot.command(name="dtc")
@commands.has_guild_permissions(manage_channels=True)
async def delete_text_channel(ctx, channel_name, category_name):
    exist_cat = discord.utils.get(ctx.guild.categories, name=category_name)
    if not exist_cat:
        await ctx.send(f"{category_name} does not exist")
        return

    exist_channel = discord.utils.get(exist_cat.text_channels, name=channel_name)
    if not exist_channel:
        await ctx.send(f"{channel_name} does not exist under {exist_cat}")
        return

    await exist_channel.delete()


@bot.command(name="nvc")
@commands.has_guild_permissions(manage_channels=True)
async def new_voice_channel(ctx, channel_name, category_name):
    exist_cat = discord.utils.get(ctx.guild.categories, name=category_name)
    if not exist_cat:
        await ctx.send(f"No specified category for the voice channel")
        return

    exist_channel = discord.utils.get(exist_cat.voice_channels, name=channel_name)
    if exist_channel:
        await ctx.send(f"{channel_name} already exists; enter another channel name")
        return

    await ctx.guild.create_voice_channel(channel_name, category=exist_cat)


@bot.command(name="dvc")
@commands.has_guild_permissions(manage_channels=True)
async def delete_voice_channel(ctx, channel_name, category_name):
    exist_cat = discord.utils.get(ctx.guild.categories, name=category_name)
    if not exist_cat:
        await ctx.send(f"{category_name} does not exist")
        return

    exist_channel = discord.utils.get(exist_cat.voice_channels, name=channel_name)
    if not exist_channel:
        await ctx.send(f"{channel_name} does not exist under {exist_cat}")
        return

    await exist_channel.delete()


@bot.command(name="new_role")
async def create_role(ctx):
    pass


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.Forbidden):
        await ctx.send("You do not have proper permissions", delete_after=15)

bot.run(TOKEN)
