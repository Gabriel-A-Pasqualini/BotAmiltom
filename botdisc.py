import discord
import asyncio 
import random 
import NHentai
import requests
import json
from hentai import Utils, Sort, Option, Tag
from pathlib import Path
from hentai import Hentai, Format

client = discord.Client()
 
palavras = {'tudo bem mano?','Aloo!','E o crurras?','Lanchão? Anima?','Não aguento mais aquarentena!','Ela te ama cara, vai em frente'}
prefix = '?'
@client.event
async def on_ready():
    print("")
    print("Hey, estou vivo!") 
    print(client.user.name)
    print(client.user.id)
    print("Let's go!")
    print(random.choice(list(palavras)))


@client.event
async def on_message(message):
        if message.author == client.user:
            return
       
        #Comandos           #=======================================================================OK
        if message.content.startswith(prefix+"comandos"):
                       channel = message.channel
                       await channel.send(" |'?ola', para dizer ola | \n |'?bot', para desejo | \n |'?to ', para marcar alguem | \n |'?hug', para receber um abraço | \n |?hentai , te recomendo um hentai/anime nsfw | \n |?dolar , para ver o Dolar hoje|")           
        
        #Ola para o Bot    #=======================================================================OK
        if message.content.startswith(prefix+"ola"):
                       channel = message.channel
                       await channel.send("Ola, suave {0.author.mention} ?".format(message))
        
        #Bot falar com  alguem marcado    #========================================================OK
        if message.content.startswith(prefix+"to"): 
                       print(message.content)
                       channel = message.channel
                       await channel.send(str(message.content).split('_O ')[1]+random.choice(list(palavras)).format(message))
                        
        #Chama o Bot   #==================================================================OK
        if message.content.startswith(prefix+'bot'): 
                       channel = message.channel
                       await channel.send("O que deseja {0.author.mention} ?".format(message))
        
        #Ser abraçado pelo Bot  #==================================================================OK
        if message.content.startswith(prefix+'hug'): 
                       channel = message.channel
                       await channel.send("Abraços {0.author.mention}".format(message))

        #Recomendação de anime +18   #=============================================================OK
        if message.content.startswith(prefix+'hentai'):
            print(Utils.get_random_hentai())
            
            hentaizao = str(Utils.get_random_hentai())

            channel = message.channel
            await channel.send( hentaizao + "\n{0.author.mention} seu hentai esta pronto ".format(message))
       
        #Mostrar o preço do dolar    #=============================================================OK
        if message.content.startswith(prefix+'dolar'): 
             channel = message.channel  
      
             def requi(vd):
                 req = requests.get('https://economia.awesomeapi.com.br/json/'+vd) 
                 dicionario = json.loads(req.text)
                 return dicionario
     
             fr = 'USD'
             moeda = requi(fr)
             await channel.send(str(moeda).split('[{')[1].split('}]')[0]+" {0.author.mention}".format(message))
            
          

with open('token.txt','r') as file:
    token = file.read().replace('\n','')

client.run(token)




