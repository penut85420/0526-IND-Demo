import os
import discord
from discord import channel
from discord.ext import commands
from pkg.utils import plus

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    ready_channel_id = int(os.getenv('READY_CHANNEL_ID'))
    channel = discord.utils.get(bot.get_all_channels(), id=ready_channel_id)
    await channel.send(f'{bot.user} | Ready!')

@bot.command(name='plus')
async def cmd_plus(ctx, a: int, b: int):
    await ctx.send(f'{a} + {b} = {plus(a, b)}')

bot.run(os.getenv('TOKEN'))
