import logging

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
channel_id = 1095177650361864303


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        return
    logging.exception(f'Error executing command "{ctx.message.content}"', exc_info=error)
    print(f'Error executing command "{ctx.message.content}": {error}')

    # Create a new file and log the error there
    with open('error.log', 'a') as f:
        f.write(f'{error} command: {ctx.message.content}\n')


@bot.event
async def on_member_join(member):
    guild = member.guild
    channel = bot.get_channel(channel_id)

    if channel is not None:
        await channel.send(f'Welcome {member.name} to {guild.name}!')
        await member.send(f'Hello {member.name}! Welcome to the {guild.name} Discord server.')


@bot.event
async def on_member_remove(member):
    guild = member.guild
    channel = bot.get_channel(channel_id)

    if channel is not None:
        await channel.send(f'Goodbye {member.name} from {guild.name}!')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def _help(ctx):
    pass


@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')


@bot.command()
async def resources(ctx):
    await ctx.send('resources')

