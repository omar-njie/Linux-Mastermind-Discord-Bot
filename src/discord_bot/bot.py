import logging

import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup


# Define the hardcoded Linux commands
# linux_commands = {
#     'ls': {
#         'usage': 'ls [OPTIONS] [FILE]',
#         'description': 'List directory contents',
#         'examples': [
#             'ls',
#             'ls -l',
#             'ls -a',
#         ]
#     },
#     'cd': {
#         'usage': 'cd [DIRECTORY]',
#         'description': 'Change directory',
#         'examples': [
#             'cd /home/user/documents',
#             'cd ..',
#             'cd ~',
#         ]
#     },
#     'mkdir': {
#         'usage': 'mkdir [OPTIONS] DIRECTORY',
#         'description': 'Make directories',
#         'examples': [
#             'mkdir directory_name',
#             'mkdir -p parent_directory/sub_directory',
#         ]
#     }
# }

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


# @bot.command()
# async def linux_command(ctx, command_name):
#     # Fetch command information from the linux_commands dictionary
#     if command_name in linux_commands:
#         command = linux_commands[command_name]
#         usage = command['usage']
#         description = command['description']
#         examples = '\n'.join(command['examples'])
#
#         # Format the response
#         embed = discord.Embed(title=f'Linux Command: {command_name}', color=discord.Color.green())
#         embed.add_field(name='Usage', value=f'```\n{usage}\n```', inline=False)
#         embed.add_field(name='Description', value=description, inline=False)
#         embed.add_field(name='Examples', value=examples, inline=False)
#         await ctx.send(embed=embed)
#     else:
#         await ctx.send(f'Error: Linux command not found.')

# linux_commands = {
#     'ls': {
#         'usage': 'ls [OPTION]... [FILE]...',
#         'description': 'List information about files and directories.',
#         'examples': ['- ls: List files and directories in the current directory.',
#                      '- ls -l: List files and directories in long format.',
#                      '- ls -a: List all files and directories, including hidden ones.']
#     },
#     'mkdir': {
#         'usage': 'mkdir [OPTION] DIRECTORY...',
#         'description': 'Create directories.',
#         'examples': ['- mkdir my_directory: Create a directory with the name "my_directory".',
#                      '- mkdir -p /path/to/directory: Create a directory with intermediate directories if they do not exist.']
#     },
#     # Add more commands here
# }
#
#
# # Command to lookup Linux commands
# @bot.command()
# async def linux_command(ctx, command_name):
#     # Fetch command information from the dictionary
#     command_info = linux_commands.get(command_name.lower())
#     if command_info:
#         usage = command_info.get('usage')
#         description = command_info.get('description')
#         examples = '\n'.join(command_info.get('examples'))
#
#         # Format the response
#         embed = discord.Embed(title=f'Linux Command: {command_name}', color=discord.Color.green())
#         embed.add_field(name='Usage', value=f'```\n{usage}\n```', inline=False)
#         embed.add_field(name='Description', value=description, inline=False)
#         embed.add_field(name='Examples', value=examples, inline=False)
#         await ctx.send(embed=embed)
#     else:
#         await ctx.send('Command not found.')

