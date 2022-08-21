
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import time
import asyncio
import random

# мой id = 252824719764619264


TOKEN = "put token here"
intents1 = discord.Intents(messages=True, guilds=True)
intents1.members = True

bot = commands.Bot(command_prefix="=", intents=intents1)
bot.remove_command('help')


# Запуск бота
@bot.event
async def on_ready():
    print('Logged in as')
    print("User name: " + bot.user.name)
    print('bot id: ' + str(bot.user.id))
    print('------')
    print("Discord API ver: " + str(discord.__version__))
    print('\nOld man is online and ready to use ;)')

#Ошибки
@bot.event
async def on_command_error(ctx, error):
    channel = ctx.message.channel
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Недостаточно аргументов")
        await asyncio.sleep(5)
        await channel.purge(limit=1)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Модуль с этим функционалом на загружен.")
        await asyncio.sleep()
        await channel.purge(limit=1)

# Цикличная смена статуса
async def chng_pr():
    status = ['=helpme для списка команд',
              'discord.py v1.5.1']
    
    await bot.wait_until_ready()
    while not bot.is_closed():
        curstat = random.choice(status)
        await bot.change_presence(activity=discord.Game(curstat))
        await asyncio.sleep(5)

# Cog load
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Cogs is loading...')

# Cog unload
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('Cogs is unloading...')

# Cog reload
@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('Cogs is reloading...')

#cogs cycle
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Logging
bot.loop.create_task(chng_pr())
bot.run(TOKEN)
