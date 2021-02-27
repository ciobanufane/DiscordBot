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
async def new_text_channel(ctx, channel_name, category_name=None):

    exist_cat = discord.utils.get(ctx.guild.categories, name=category_name)
    if category_name and not exist_cat:
        await ctx.send(f"Category \"{category_name}\" does not exist")
        return

    exist_channel = discord.utils.get(ctx.guild.text_channels, name=channel_name, category=exist_cat)
    if exist_channel:
        await ctx.send(f"Text channel \"{channel_name}\" already exists under category: {category_name}\n"
                       f"Enter a unique channel name")
    else:
        await ctx.guild.create_text_channel(channel_name, category=exist_cat)


@bot.command(name="rtc")
@commands.has_guild_permissions(manage_channels=True)
async def remove_text_channel(ctx, channel_name, category_name=None):

    exist_cat = discord.utils.get(ctx.guild.categories, name=category_name)
    if category_name and not exist_cat:
        await ctx.send(f"Category \"{category_name}\" does not exist")
        return

    exist_channel = discord.utils.get(ctx.guild.text_channels, name=channel_name, category=exist_cat)
    if exist_channel:
        await ctx.send(f"Deleting text channel \"{channel_name}\" under category: {category_name}")
        await exist_channel.delete()
    else:
        await ctx.send(f"Text channel \"{channel_name}\" does not exist under category: {category_name}")


@bot.command(name="nvc")
@commands.has_guild_permissions(manage_channels=True)
async def new_voice_channel(ctx, channel_name, category_name=None):

    exist_cat = discord.utils.get(ctx.guild.categories, name=category_name)
    if category_name and not exist_cat:
        await ctx.send(f"Category \"{category_name}\" does not exist")
        return

    exist_channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name, category=exist_cat)
    if exist_channel:
        await ctx.send(f"Voice channel \"{channel_name}\" already exists under category: {category_name}\n"
                       f"Enter a unique channel name")
    else:
        await ctx.guild.create_voice_channel(channel_name, category=exist_cat)


@bot.command(name="rvc")
@commands.has_guild_permissions(manage_channels=True)
async def remove_voice_channel(ctx, channel_name, category_name=None):

    exist_cat = discord.utils.get(ctx.guild.categories, name=category_name)
    if category_name and not exist_cat:
        await ctx.send(f"Category \"{category_name}\" does not exist")
        return

    exist_channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name, category=exist_cat)
    if exist_channel:
        await ctx.send(f"Deleting voice channel \"{channel_name}\" under category: {category_name}")
        await exist_channel.delete()
    else:
        await ctx.send(f"Voice channel \"{channel_name}\" does not exist under category: {category_name}")


@bot.command(name="new_role")
async def create_role(ctx):
    pass


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.Forbidden):
        await ctx.send("You do not have proper permissions", delete_after=15)

bot.run(TOKEN)
