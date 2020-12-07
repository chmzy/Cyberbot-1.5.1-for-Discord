import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import db.char_dict
import db.pivo_dict
import db.serv_id_dict
import db.tutu_id_dict


class Parser(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Погода
    @commands.command()
    async def погода(self, ctx, city):
        channel = ctx.message.channel
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=fb1614a705527b4c51bba4cb79e40664&units=metric'.format(city)
    
        res = requests.get(url)
        data = res.json()
        embed = discord.Embed(colour=discord.Color.red())
        description = data['weather'][0]['description']
        #main = data['weather'][0]['main']
        temp = data['main']['temp']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
    
        embed.set_author(name='Какая сейчас погода в {}'.format(city))
        embed.add_field(name='Погодные условия', value=description, inline=False)
        embed.add_field(name='Температрура, ℃', value=temp, inline=True)
        embed.add_field(name='Давление, Па', value=pressure, inline=True)
        embed.add_field(name='Скорость ветра, м/c', value=wind_speed, inline=True)
        
        async with ctx.typing():
            await ctx.send('Получаю достоверную информацию...')
            await asyncio.sleep(2)
            await channel.purge(limit=1)
            await ctx.send(embed=embed)
    
    #кто ты из смешариков
    @commands.command(aliases=['smesharik'])
    async def kekorik(self, ctx, member: discord.Member = None):
        random.seed(datetime.now())
        a = random.choice(list(char_dict.kek_chimps))  
        b = char_dict.kek_chimps.get(a)
        embed = discord.Embed(title=f"{member.name}, ты - {a}", color=discord.Color.blue(), inline=True)
        embed.set_image(url=b)
        await ctx.send(embed=embed)
    
    #кто ты из ЛОЛА
    @commands.command()
    async def randlol(self, ctx, member: discord.Member = None):
        random.seed(datetime.now())
        ans = [' тебе подходит', ' рандом подобрал тебе',
               ' твоя копия -', ' сегодня играешь на']
        a = random.choice(list(char_dict.lol_chimps))
        b = char_dict.lol_chimps.get(a)
        c = random.choice(ans)
        embed1 = discord.Embed(title=f"{member.name}, {c} **{a}**", color=discord.Color.teal(), inline=True)
        embed1.set_image(url=b)
        await ctx.send(embed=embed1)
    
    #lol_role_assign_v2.0
    @commands.command(aliases=['lul'])
    async def lol(self, ctx, role , member: discord.Member = None):
        channel = ctx.message.channel
        role_s = str(role).capitalize()
    
        random.seed(datetime.now())
        role_rand = ["Топ", "Лес", "Мид", "Адк", "Сап"]
    
        ans_top = ['сегодня на топе разносишь за', 'кто-то сегодня будет сосать на топе за', 'осторожней на топе, играешь на']
        ans_jun = ['лучший фармила в LOLe - это', 'сосешь в лесу за', 'быстрее на Синих Стражей за']
        ans_mid = ['осторожней на миду за', 'передавай Пуджу привет за', 'сливаешь фб на ', 'остерегайтесь петухов на миду за']
        ans_adc = ['хороший адк за свои средства это', 'АДК на боте - враг в заглоте, пикаешь', 'сегодня фидишь на']
        ans_sup = ['саппорт - не человек, пикаешь', 'сап двач, ты ламповая', 'замещаешь курьера за']
        
        #if role_s.upper() == 'РАНД':
        #    role_s = random.choice(role_rand)
        #    fin = 'рандом'
        if role_s.upper() == 'TOP':
            role_s = role_rand[0]
            fin = random.choice(ans_top)
        if role_s.upper() == 'JUNG':
            role_s = role_rand[1]
            fin = random.choice(ans_jun)
        if role_s.upper() == 'MID':
            role_s = role_rand[2]
            fin = random.choice(ans_mid)
        if role_s.upper() == 'ADC':
            role_s = role_rand[3]
            fin = random.choice(ans_adc)
        if role_s.upper() == 'SUP':
            role_s = role_rand[4]
            fin = random.choice(ans_sup)
    
        name = random.choice(list(char_dict.lol_roles_chimps[role_s]))
        ava = char_dict.lol_roles_chimps[role_s][name]
        
        embed1 = discord.Embed(title=f"{member.name}, {fin} **{name}**", color=discord.Color.teal(), inline=True)
        embed1.set_image(url=ava)
        embed1.set_footer(text = f'{str(member.name)} присвоена роль {role_s}', icon_url = member.avatar_url)
        
        async with ctx.typing():
            await ctx.send('Чекаю твой ммр...')
            await asyncio.sleep(2)
            await channel.purge(limit=1)
            await ctx.send(embed=embed1)
        
    #Беру-выходной :)
    @commands.command(aliases=['buh'])
    async def w2dr(self, ctx, member: discord.Member = None):
        if (member.id == 257802832911138816):  # '257802832911138816'
            ans = ['**водички** нам принеси, вот тебе **бокальчик**']
            url1 = 'https://sochi.com/upload/resize_cache/iblock/4f8/800_800_1/detskoe_shampanskoe.jpg'
            url2 = 'https://pliki.portalspozywczy.pl/i/07/49/78/074978_940.jpg'
            embed1 = discord.Embed(title=f'{member.name}, вот тебе **бокальчик**', colour=discord.Color.red())
            embed1.set_image(url=url1)
            await ctx.send(embed=embed1)
        else:
            random.seed(datetime.now())
            name = random.choice(list(pivo_dict.piv4))
            piv_alc = pivo_dict.piv4.get(name)[0]
            piv_price = pivo_dict.piv4.get(name)[1]
            url_serarch = f'https://winestyle.ru/catalog/?search_query={name.replace(" ","%C2%A0")}'
            url_gugl = f'https://www.google.com/search?client=firefox-b-d&q={name.replace(" ","+")}'
            #url_serarch = f'https://krasnoeibeloe.ru/catalog/?q={name.replace(" ","_")}'
            embed = discord.Embed(title=f'{member.name}, сегодня пьешь {name}', colour=discord.Color.teal())
            embed.add_field(name='Алк, %', value=piv_alc, inline=False)
            embed.add_field(name='Цена, руб', value=piv_price, inline=True)
            embed.add_field(name='Ссылка', value=url_serarch, inline=True)
            embed.add_field(name='Гугл', value=url_gugl, inline=True)
            embed.set_image(url='https://yandex.ru/images/_crpd/nU5Up2200/56026eQiNg/kQJJ95MqXH-wLbDXGTSM5BJpQiHo7M9DRxLNyLCT-_3lX_ZbxJf-qPpSrqr7HjrJX5k7XuRulmodG4vEcR03Z8EDV6WHJQE2oHu5i0YPtt19RXgalcy3Y21WlMW3kuewpE-fMdP3v_OfDfPw3HdrxDOpfX-xfIM7QUTu13QmdmOXcDDWliEUe5NNm8E_KJPXaGVQBJLjokVqd4zniZjQ2o52lx-h45XlsxTn0PZoWsAOqn5Jsl2UO3deyNN9ClR4k14szqg5PHSXb4zCEjiA0nFqaCyM6odtaGGm-7eF-u2-Sacdi8Sr7okX7drya17cDZRNV7pHogtvW_TKUDtqQYV_FPuDIhZfqm2wxCAhpthQZHIBo-GmfHZ3udymvNPQuGK5D7nwmu-kNen9yHd_-wGNfGWbWJ8rXWPV7nMmVl-7fz7AlREAZ45uu_MfFIbvfUJgIajql2lydaX9v7z93YN3oRqW057fvyrV2-53Tt0VlWVUjFCgIkpOyeRxOk9HkVYWz64kElSpT5__IiaPyG1Icj-3zJtzaVqn2qWt_PKRdpEqpOe7z58kzef8bErNAYBkarZYohFpVuDVZQ5Ic4RTFsavDBZggGuN9DY-osxpVGgHo--USHJYtOWkgNbdp3WDIZnSg-6pBM3y1n5QxBKIcG-jTpouSlba9lEFfES9RgrVgSUhRqFRpf8zE5_eeGBFPqjktl92ZKzsvpzO1aBDsRyW1r_oozfq1exrZuUprlhWvFq9P0Nk4tN2PU9GqkoT4ZQBJmS_UbHGMRih721MUhKe4YRSQG6Zzrej8dyDc6cNuNWF97Ir29XmSkrTKrVFUJlDvg9EXuPxXg9BWoxWJtORGTpjk0iP0yAxvMhZVEEwguqqZWp2gPiUp8zIk3aaHJXEjte_FeX-8Hdt7QmZfFaYY7MoWFvJ6X0CT22TWCfhkSYYYolxm-8wAJ3Xf1dfObTOqmRbQ7LRp5s')
            await ctx.send(embed=embed)
    
    #рандомная цитата
    @commands.command()
    async def quote(self, ctx):
        url = 'https://citaty.info/random'
        myheader = {}
        myheader['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.3.281 Yowser/2.5 Safari/537.36'
        html = requests.get(url, headers=myheader).text
        soup = BeautifulSoup(html, 'lxml')
        first = soup.find("div", class_="field-item even last").text
        embed_l = discord.Embed(title=f'{first}', colour=discord.Color.teal())
        await ctx.send(embed=embed_l)
    
    #туту.ру
    @commands.command()
    async def tutu(self, ctx, town):
        town_id = tutu_id_dict.tutu_dict.get(town)
        url = f'https://www.tutu.ru/rasp.php?st1={town_id}&st2=80410&date=02.12.2020'
        myheader = {}
        myheader['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.3.281 Yowser/2.5 Safari/537.36'
        html = requests.get(url, headers=myheader).text
        soup = BeautifulSoup(html, 'lxml')
        elka = soup.find("div", class_="b-etrain__price_block l-etrain__price_block").find('span', class_ = 'price_big_txt').text
        l4 = soup.find("div", class_ = 'b-etrain__price_block_firm l-etrain__price_block_firm j-price_block_firm').find('span', class_ = 'g-link _pseudo _dark j-price_link prevent_select').text
        await ctx.send(f'Обычная - {elka}, Ласточка - {l4}')


def setup(bot):
    bot.add_cog(Parser(bot))
    print('Класс Parser создан\n')
