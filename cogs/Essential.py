import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
from datetime import datetime


class Essential(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    #Комманда help
    @commands.command()
    async def helpme(self, ctx):
        author = ctx.message.author
        embed_help = discord.Embed(colour=discord.Color.green())
        embed_help.set_author(name='Список команд')
        embed_help.add_field(name='**ОСНОВЫ**', value ="", inline=False)
        embed_help.add_field(name='`=greet @упоминание`',value='Приветствует того, кого вы указали', inline=False)
        embed_help.add_field(name='`=ava @упоминание`', value='Кидает прямую ссылку на аватарку пользователя', inline=False)
        embed_help.add_field(name='`=say сообщение`', value='Повторяет за вами сообщение', inline=False)
        embed_help.add_field(name='`=delyt n, (n - целое число)`', value='Удаляет последние **n** сообщений', inline=False)
        embed_help.add_field(name='`=погода (название города на *английском*)`', value='Выводит табличку с полным описанием погоды на данный момент в данном городе', inline=False)
        embed_help.add_field(name='**ТЕСТИКИ**', value="", inline=False)
        embed_help.add_field(name='`=coolcheck @упоминание`', value='Проводит тест крутость', inline=False)
        embed_help.add_field(name='**Бог рандома**', value="", inline=False)
        embed_help.add_field(name='`=kekorik/smesharik @упоминание`', value='Узнай кто из Смешариков тебе больше всего подходит!', inline=False)
        embed_help.add_field(name='`=randlol @упоминание`', value='Позвольте рандому подобрать вам чемпиона для игры в League of Legends!', inline=False)
        embed_help.add_field(name='`=lol role @упоминание`', value='Рандом подберет вам персонажа под вашу role, исходя из вашего ммр :)\n Доступные role: топ, мид, адк, лес, сап', inline=False)
        embed_help.add_field(name='`=w2dr/buh @упоминание`', value='Позволь рандому подобрать тебе напиток на этот вечер из каталога "Беру выходной!"', inline=False)
    
        await ctx.author.send(author, embed=embed_help)
    
    # Повторение слов
    @commands.command()
    async def say(self, ctx, *, words):
        channel = ctx.message.channel
        messages = []
        async for message in channel.history(limit=1):
            messages.append(message)
        await channel.delete_messages(messages)
        await ctx.send(words)
    
    # Приветствие в две стороны
    @commands.command()
    async def greet(self, ctx, member: discord.Member = None):
        if ctx.message.author.id == 252824719764619264:
            await ctx.send(f"Ежжи как жизнь, {member.mention} <:kama:336765358448967683>")
        else:
            await ctx.send(f"{ctx.author} передает тебе, {member.mention}, привет!")

     #Очистка сообщений
    @commands.command(pass_contex=True)
    async def delyt(self, ctx, amount=1000):
        channel = ctx.message.channel
        messages = []
        async for message in channel.history(limit=int(amount) + 1):
            messages.append(message)
        if ctx.message.author.id == 252824719764619264 or ctx.message.author.id == 432153138758287360:
            await channel.delete_messages(messages)
            await ctx.send('👌' + 'Удалены последние ' + str(amount) + ' сообщений', delete_after=1)

    #создание ролей
    @commands.command(aliases=['wb'])
    async def wannabe(self, ctx, *, names):
        guild = ctx.guild
        channel = ctx.channel
        await channel.purge(limit=1)
        await guild.create_role(name=names, color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        await ctx.send("Done!")
        await asyncio.sleep(2)
        await channel.purge(limit=1)
    
    
    #счетчик ролей
    @commands.command()
    async def rolecount(self, ctx, member: discord.Member = None):
        #guild = ctx.guild
        n = 0
        for _ in member.roles:
            n += 1
        await ctx.send(f'{member.name} имеет при себе **{n-1}** ролей!')
    
    #Аватарка пользователя
    @commands.command()
    async def ava(self, ctx, member: discord.Member = None):
        await ctx.send(member.avatar_url)

    #Законы робототехники
    @commands.command()
    async def robotech_laws(self, ctx):
        await ctx.send("""1. роБ0т не может причинить вред человеку или своим бездействием допустить, чтобы человеку был причинён вред.""")
        await asyncio.sleep(0.5)
        await ctx.send("""2. роБ0т должен повиноваться всем приказам, которые даёт человек, кроме тех случаев, когда эти приказы противоречат Первому Закону.""")
        await asyncio.sleep(0.5)
        await ctx.send("""3. роБ0т должен заботиться о своей безопасности в той мере, в которой это не противоречит Первому или Второму Законам.""")


def setup(bot):
    bot.add_cog(Essential(bot))
    print('Класс Essential создан\n')
