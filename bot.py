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
    watch = discord.Activity(type=discord.ActivityType.watching, name="my life go away")
    await bot.change_presence(status=discord.Status.idle, activity=watch)


@bot.command(name='echo', aliases=["e"])
async def echo(ctx, *, message: str):
    if str(ctx.channel.id) == TEST:
        await ctx.send(message, delete_after=15)


@bot.command(name="new-category", aliases=["nc"])
@commands.has_guild_permissions(manage_channels=True)
async def new_category(ctx, *, category_name: str):
    exist_cat = discord.utils.get(ctx.guild.categories, name=category_name)

    if exist_cat:
        await ctx.send(f"The category, \"{category_name}\", already exists.")
        return

    await ctx.guild.create_category(category_name.upper())


@bot.command(name="remove-category", aliases=["rc"])
@commands.has_guild_permissions(manage_channels=True)
async def remove_category(ctx, *, category_name: str):
    category_name = category_name.upper()

    exist_cat = discord.utils.get(ctx.guild.categories, name=category_name)

    if not exist_cat:
        await ctx.send(f"The category, \"{category_name}\", does not exist.")
        return

    if exist_cat.channels:
        await ctx.send(f"The category, \"{category_name}\", still contains channels. "
                       f"\nPlease delete the channels before removing the category.")
    else:
        await exist_cat.delete()


@bot.command(name="new-textchannel", aliases=["ntc"])
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


@bot.command(name="remove-textchannel", aliases=["rtc"])
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


@bot.command(name="new-voicechannel", aliases=["nvc"])
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


@bot.command(name="remove-voicechannel", aliases=["rvc"])
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


@bot.command(name="new-role", aliases=["nr"])
@commands.has_guild_permissions(manage_roles=True)
async def new_role(ctx, role_name):
    pass


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.MissingPermissions):
        await ctx.send("You need the permissions:\n{}".format("\n".join(error.missing_perms)), delete_after=15)

bot.run(TOKEN)
