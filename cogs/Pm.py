import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import requests
from datetime import datetime
import sys
sys.path.append('C:\\DisBot\\cyberbot_oop\\db')
import serv_id_dict


class Pm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #парсинг idшек
    @commands.command()
    async def idprs(self, ctx):
        channel = ctx.message.channel
        await channel.purge(limit=1)
        VCC = discord.utils.get(ctx.guild.channels, id=channel.id)
        ids = {}
    
        for user in VCC.members:
            ids[user.name] = f'{user.id}'

        print(ids)
    
    
    #серверная-рассылка
    @commands.command()
    async def warn(self, ctx, v, *, message):
        channel = ctx.message.channel
        await channel.purge(limit=1)
    
        id_list = [serv_id_dict.id_chms, serv_id_dict.id_krab, serv_id_dict.id_slav]
        id_based = {}
        id_based = id_list[int(v)]
        n = 0
        names = list(id_based)
    
        print(f'{len(id_based)} members will recieve message!')
        for _ in range(len(names)):
            id_c = id_based.get(names[n])  # id_c = .id; names[n] = .name
            namae = self.bot.get_user(int(id_c))
            await namae.send(f'{message}')
            print(f"{namae} recieved message")
            n += 1
    
        print("----------\nfinished message spam")


def setup(bot):
    bot.add_cog(Pm(bot))
    print('Класс PM создан\n')
