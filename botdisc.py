import discord
import asyncio
import random
import NHentai
import requests
import json
#import mysql.connector
import psutil  # Puxa os dados do computador
import time
import apostas
import psycopg2  # import do bd postgres
import themovie

from themovie import requisicao, printar_detalhes

from pagando import pagamento

from PIL import Image

from apostas import Saldo, Bicho

from federal import primeiro

from discord.ext import commands
from discord import Embed, Member
from discord.ext.commands import Cog
from discord.ext.commands import command
from hentai import Utils, Sort, Option, Tag
from pathlib import Path
from hentai import Hentai, Format


banco = psycopg2.connect(
    user="postgres",
    password="123",
    host="127.0.0.1",
    port="5432",
    database="discord"
)


client = discord.Client()


palavras = {'tudo bem mano?', 'Aloo!', 'E o crurras?', 'Lanchão? Anima?',
            'Não aguento mais aquarentena!', 'Ela te ama cara, vai em frente'}

prefix = '?'
aspas = "```"

client = commands.Bot(command_prefix='?')

'''
@client.command
async def kick(ctx , member : discord.Member, * ,reason = None):
    await member.kick(reason = reason)
'''


@client.event
async def on_ready():
    print("")
    print(f'{client.user} has connected to Discord!')
    print(client.user.name)
    print(client.user.id)
    print("Let's go!")
    print(random.choice(list(palavras)))
    print('')
    print('')
    print('')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Comandos           #=======================================================================OK
    if message.content.startswith(prefix+"comandos"):
        channel = message.channel
        await channel.send(aspas+" |?hentai , te recomendo um hentai/anime nsfw | \n |?dolar , para ver o Dolar hoje| \n |?cpu, porcentagens da CPU| \n |?registro, para que eu te registre| \n |?filme (nome do filme em ingles), para mostrar detalhes do filme| \n |?tabela, para ver a tabela do jogo do bicho"+aspas)

    # Recomendação de anime +18   #=============================================================OK
    if message.content.startswith(prefix+'hentai'):
       # print(Utils.get_random_hentai())

        hentaizao = str(Utils.get_random_hentai())

        channel = message.channel
        await channel.send(hentaizao + "\n{0.author.mention} seu hentai esta pronto ".format(message))

    # Mostrar o preço do dolar    #=============================================================OK
    if message.content.startswith(prefix+'dolar'):
        channel = message.channel

        def requi(vd):
            req = requests.get('https://economia.awesomeapi.com.br/json/'+vd)
            dicionario = json.loads(req.text)
            return dicionario

        fr = 'USD'
        moeda = requi(fr)
        await channel.send(str(moeda).split('[{')[1].split('}]')[0]+" {0.author.mention}".format(message))

    # Mostrar filme  #========================================================================OK
    if message.content.startswith(prefix+'filme'):
        channel = message.channel
        op = requisicao(message.content.split('filme ')[1])

        if op['Response'] == 'False':
            await channel.send('Nao deu certo').format(message)
        else:
            movie = printar_detalhes(op)

            for i in range(0, len(movie)):

                if i == len(movie)-1:
                    await channel.send(str(movie[i]))

                else:
                    await channel.send(aspas+str(movie[i])+aspas)

    # Registro no banco  #====================================================================OK
    if message.content.startswith(prefix+'registro'):
        #print(message.content.split('registro ')[1])
        channel = message.channel

        await channel.send("farei seu registro {0.author.mention}".format(message))

        author = message.author

        target = author

        print(target.name)
        print(target.id)

        name = (target.name)

        nume = (target.id)  # ID
        try:
            comando_SQL = "INSERT INTO user_discord (id, nome, dinheiro) VALUES (%s,%s, 500)"
            dados = (nume, name)

            cursor = banco.cursor()

            cursor.execute(comando_SQL, dados)

            banco.commit()

            await channel.send(aspas+"registro feito"+aspas.format(message))
        except:
            await channel.send("registro de  {0.author.mention} FALHO".format(message))

    # Apostas jogo do bicho = saldo #===========================================================OK
    if message.content.startswith(prefix+'saldo'):
        channel = message.channel

        author = message.author
        target = author
        print(target.name)
        print(target.id)
        print(message.content)

        await channel.send("{0.author.mention} mostrarei seu dinheiro".format(message))

        try:
            vitao = Saldo(target.id)
            await channel.send(aspas+"voce tem $"+str(vitao).split("'")[1].split("'")[0]+aspas.format(message))

        except:

            await channel.send("{0.author.mention} a consulta falhou".format(message))

    # Apostas jogo do bicho = tabela #===========================================================OK
    if message.content.startswith(prefix+'tabela'):
        channel = message.channel

        img = Image.open('TABELADOJOGODOBICHO.jpeg')
        # img.show() 'abre a imagem'

        try:

            await channel.send(file=discord.File('TABELADOJOGODOBICHO.jpeg'))
            await channel.send(aspas+'é em qual meu patrão?'+aspas.format(message))

        except:

            await channel.send(img)

    # Apostas jogo do bicho = aposta ===========================================================OK
    if message.content.startswith(prefix+'aposta '):

        aposta = message.content.split('. ')[1]
        numero_bicho = message.content.split('aposta ')[1].split('.')[0]

        channel = message.channel

        author = message.author

        target = author

        teste = Bicho(numero_bicho)

        await channel.send('apostando...')

        if teste == 0:
            await channel.send(aspas+'ERRO! Bicho nao encontrado'+aspas.format(message))

        else:
            try:
                data = time.ctime()

                comando_SQL = "INSERT INTO aposta (id_user, dinheiroapostado, data, bicho) VALUES (%s,%s,%s,%s)"
                dados = (target.id, aposta, data, str(teste))

                cursor = banco.cursor()

                cursor.execute(comando_SQL, dados)

                banco.commit()

                await channel.send(aspas+'voce apostou no: '+str(teste)+aspas.format(message))

                try:
                    comando = "UPDATE user_discord SET dinheiro = (dinheiro - %s) WHERE id = '%s'"
                    testinhno = (aposta, target.id)

                    cursor.execute(comando, testinhno)

                    banco.commit()

                    await channel.send(aspas+'deu certo'+aspas.format(message))
                except:
                    await channel.send(aspas+'nao contou'+aspas.format(message))

            except:

                await channel.send(aspas+'ERRO!'+aspas.format(message))

    # Apostas jogo do bicho = resultado =========================================================OK

    if message.content.startswith(prefix+'bicho vencedor'):
        channel = message.channel

        await channel.send('O bicho vencedor é o '+primeiro)

    # Aposta jogo do bicho = pagando   ==========================================================OK
    if message.content.startswith(prefix+'conferir'):
        channel = message.channel

        author = message.author
        target = author
        print(target.name)
        print(target.id)
        x = pagamento(target.id)

        await channel.send(x)

    # Imagem foda ===============================================================================OK
    if message.content.startswith(prefix+'miguel'):
        channel = message.channel

        await channel.send('https://i.pinimg.com/originals/32/60/bf/3260bf5b2bb23034535fa9d5c20ddcab.jpg')

    # % da CPU #================================================================================OK
    if message.content.startswith(prefix+'cpu'):
        channel = message.channel
        siistema = str(psutil.virtual_memory()._asdict())
        ssitema = str(psutil.cpu_percent())
        await channel.send("CPU: "+ssitema+'\nMemoria ram: '+siistema+'\nData:  '+time.ctime()+"\n{0.author.mention}".format(message))


with open('token.txt', 'r') as file:
    token = file.read().replace('\n', '')
client.run(token)
