import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
from datetime import datetime


class Chatrand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Тест на крутость
    @commands.command()
    async def coolcheck(self, ctx, member: discord.Member = None):
        if member.id == 319170886345162754:
            ans1 = [f"{member.name} несомненно круче всех!",
                    f"{member.name}, вы самый крутой на сервере."]
            embed1 = discord.Embed(title=random.choice(
                ans1), color=discord.Color.blue(), inline=True)
            await ctx.send(embed=embed1)
        else:
            percent = random.randint(0, 100)
            ans = [f"Оказывается, {member.name} крутой на {percent}%",
                   f"Факт - {member.name} превосходит любого на {percent}%"]
            embed2 = discord.Embed(title=random.choice(
                ans), color=discord.Color.blue(), inline=True)
            await ctx.send(embed=embed2)


def setup(bot):
    bot.add_cog(Chatrand(bot))
    print('Класс Chatrand создан\n')
