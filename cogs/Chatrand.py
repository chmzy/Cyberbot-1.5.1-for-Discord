import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
from datetime import datetime


class Chatrand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Тест на пидора
    @commands.command()
    async def pdr(self, ctx, member: discord.Member = None):
        answers = [
            f"Мне кажется, или человек с именем **{member.name}** по определению пидор? 🤔",
            f"<:moon:334034106516242436> **{member.name}**, Однозначно вы натурал 😎",
            f"👌 Без сомнений, **{member.name}** пидор 👌 ",
            f"**{ctx.author.name}** А может ты пидор?"
        ]
    
        message = random.choice(answers)
        embed = discord.Embed(title=message, color=discord.Color.blue(), inline=True)
        await ctx.send(embed=embed)
    
    #Тест на левачество
    @commands.command()
    async def levak(self, ctx, member: discord.Member = None):
        if member.id == 319170886345162754:
            ans1 = [f"{member.name}, Байден бы тебе отсосал - ЛЕВЫЙ на 100%",
                    f"{member.name}, без сомнений, вы ЛЕВАК на 100%"]
            embed1 = discord.Embed(title=random.choice(
                ans1), color=discord.Color.blue(), inline=True)
            await ctx.send(embed=embed1)
        else:
            percent = random.randint(0, 100)
            ans = [f"Оказывается, {member.name} левый на {percent}%",
                   f"Факт - {member.name} левый на все {percent}%"]
            embed2 = discord.Embed(title=random.choice(
                ans), color=discord.Color.blue(), inline=True)
            await ctx.send(embed=embed2)


def setup(bot):
    bot.add_cog(Chatrand(bot))
    print('Класс Chatrand создан\n')
