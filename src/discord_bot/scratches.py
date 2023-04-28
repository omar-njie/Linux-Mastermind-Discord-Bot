# Command to lookup Linux commands
# @bot.command()
# async def linux_command(ctx, command_name):
#     """Look up details for a Linux command"""
#     url = f'https://man7.org/linux/man-pages/man1/{command_name}.1.html'
#     response = requests.get(url)
#     html = response.text
#
#     # Extract description
#     desc_start = html.find('<h2><a name="DESCRIPTION">DESCRIPTION</a></h2>')
#     desc_end = html.find('<h2><a name="OPTIONS">OPTIONS</a></h2>', desc_start)
#     description = html[desc_start + len('<h2><a name="DESCRIPTION">DESCRIPTION</a></h2>'):desc_end].strip()
#
#     # Extract usage
#     usage = html[html.find('<h2><a name="SYNOPSIS">SYNOPSIS</a></h2>') + len('<h2><a name="SYNOPSIS">SYNOPSIS</a></h2>'):].split('\n')[0].strip()
#
#     # Extract examples
#     examples_start = html.find('<h2><a name="EXAMPLES">EXAMPLES</a></h2>')
#     examples_end = html.find('</body></html>', examples_start)
#     examples = html[examples_start + len('<h2><a name="EXAMPLES">EXAMPLES</a></h2>'):examples_end].strip()
#     examples = '\n'.join([ex.strip() for ex in examples.split('<p>')])
#
#     # Embed response
#     embed = discord.Embed(title=f'{command_name.upper()} command')
#     embed.description = description
#     embed.add_field(name='Usage', value=usage, inline=False)
#
#     # Split examples into multiple fields
#     examples = examples.split('\n')
#     for i in range(0, len(examples), 25):  # Split examples into chunks of 25 examples
#         embed.add_field(name='Examples', value='\n'.join(examples[i:i + 25]), inline=False)
#
#     await ctx.send(embed=embed)
#
