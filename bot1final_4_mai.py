#!/usr/bin/env python3
# -- coding: utf-8 --

import sys
import discord
from discord.ext import commands
import asyncio

my_channel_id = 705073195077730344

BOTman_id = 705418360216748062

myAuthorId = 476338851871326219

nbQ1gagnant = 0
nbQ2gagnant = 0
top10IdsQ1 = []
top10IdsQ2 = []
ontBonMaisTropTardQ1 = []
ontBonMaisTropTardQ2 = []
perduAnImporteQuelQ = []
nepasbloquerq1=True # pour ne pas bloquer q1
nepasbloquerq2= True# pour ne pas bloquer q2
####
# Events
####
client = commands.Bot(command_prefix='.')

#challenge rép
rep1='1) Linux Mint'
rep2='2) Google Images -> Insérer image -> Rechercher'

#reponse du bot
gagnepremiereq='Vous avez gagné à la première question'
gagnedeuxiemeq='Vous avez gagné à la deuxième question'

# rep triche:
reptriche1='Vous avez déjà participé ! Faîtes autre chose !!'
reptriche2='tente de tricher!!'
#reponse si trop tard du bot
repbotlate1='Désolé mais 10 autres personnes ont déjà gagné'
repbotlate1bis='Soyez plus rapide à la prochaine question '

#définition des fonctions
def reptricheur(top10IdsQx, repx, nepasbloquerqx, msg):
    if msg.author.id in top10IdsQx and msg.content.casefold()== repx.casefold() :
        msg.channel.send(reptriche1)
        print(msg.author.id, reptriche2)
        nepasbloquerqx=False # valeur qui bloque la questionx si l'utilisateur tente de rerépondre bon
        return False
    else: 
        nepasbloquerqx=True
        return True

        #casefold pour ignorer la casse majuscule, minuscule ou mélangées
def repondre_jusqua10(msg, repx, top10IdsQx, nepasbloquerqx,nbQxgagnant, ontBonMaisTropTardQx):
    if msg.content.casefold() ==repx.casefold() and reptricheur(top10IdsQx, repx, nepasbloquerqx , msg)==True:
        # await msg.channel.send(gagnepremiereq)
        print(msg.author.id)
        top10IdsQx.append(msg.author.id)
        nbQxgagnant += 1
        return True
        if nbQ1gagnant == nbQxgagnant :
            print('gagné q1=', nbQ1gagnant)
        elif nbQ2gagnant == nbQxgagnant :
            print('gagné q2=', nbQ2gagnant)

@client.event
async def on_ready():
    print ('Challenge Bot est prêt.')
    return True        

@client.event
async def on_message(message):
    try:
        global appel_membre, appel, absents, presents

        global nbQ1gagnant, nbQ2gagnant, top10IdsQ1, top10IdsQ2, ontBonMaisTropTardQ1, ontBonMaisTropTardQ2, perduAnImporteQuelQ, nepasbloquerq1, nepasbloquerq2
        if message.author.id != BOTman_id:
            print("Je suis", message.author.id)
            print("Actuellement les valeurs sont :")
            print("my_channel_id, BOTman_id, myAuthorId", \
                my_channel_id, BOTman_id, myAuthorId)
            print("nbQ1gagnant, nbQ2gagnant, top10IdsQ1,top10IdsQ2, ontBonMaisTropTardQ1, ontBonMaisTropTardQ2, perduAnImporteQuelQ")
            print(nbQ1gagnant, nbQ2gagnant, top10IdsQ1, top10IdsQ2, ontBonMaisTropTardQ1, ontBonMaisTropTardQ2, perduAnImporteQuelQ)
            print("Message initial", message)

        # Pour les personnes qui peuvent lancer le Challenge
        if message.content == 'Challenge!!' \
            and message.author.id in (myAuthorId, 689134480291528710, 480045172630224916) :
            await message.channel.send('coucou Challenge 1 : Savez-vous comment s appelle mon logo')
            await message.channel.send('Si non faites un reverse search sur Google ou BING ')
            await message.channel.send('Réponse sous la forme : en MP')
            await message.channel.send('1) Google Chrome //ne pas oublier le numéro la parenthèse et l espace et majuscule')
        elif message.content == '!!Challenge' \
            and message.author.id in (myAuthorId, 689134480291528710, 480045172630224916) :    
            await message.channel.send('Challenge 2 : Comment faire le reverse search ?')
            await message.channel.send('Réponse sous la forme : en MP')
            await message.channel.send('2) Google Chrome -> Téléchargement -> Cliquer sur le fichier téléchargé //ne pas oublier le numéro la parenthèse et l espace et majuscule')
        
        # Dans le channel privée et si ce n'est pas le bot
        if isinstance(message.channel, discord.DMChannel) and message.author.id != BOTman_id :
            print("Message privé : " + message.content)
            
            # reptricheur(top10IdsQ1, rep1, nepasbloquerq1,message) #si un user tente de rerépondre Q1
            # reptricheur(top10IdsQ2, rep2, nepasbloquerq2,message)         #si user tente de rerépondre Q2    
            # if message.content.casefold() == rep1.casefold() and nepasbloquerq1!=False: #casefold pour ignorer la casse majuscule, minuscule ou mélangées
            # if message.content.casefold() == rep1.casefold() and reptricheur(top10IdsQ1, rep1, nepasbloquerq1,message)==True: 


            repondre_jusqua10(message, rep1, top10IdsQ1, nepasbloquerq1, nbQ1gagnant, ontBonMaisTropTardQ1)
            # await message.channel.send(gagnepremiereq)
            # if repondre_jusqua10 == True :
            #     await message.channel.send(gagnepremiereq)
                
            repondre_jusqua10(message, rep2, top10IdsQ2, nepasbloquerq2, nbQ2gagnant, ontBonMaisTropTardQ2)
            
            if nbQ1gagnant > 10:
                await message.channel.send(repbotlate1)
                await message.channel.send(repbotlate1bis)
                ontBonMaisTropTardQ1.append(message.author.id)

            # elif message.content.casefold() == rep2.casefold() and reptricheur(top10IdsQ2, rep2, nepasbloquerq2,message):
            #     await message.channel.send(gagnedeuxiemeq)
            #     print(message.author.id)
            #     top10IdsQ2.append(message.author.id)
            #     nbQ2gagnant += 1
            #     print('gagné q2=', nbQ2gagnant)

                if nbQ2gagnant > 10:
                    await message.channel.send(repbotlate1)
                    await message.channel.send(repbotlate1bis)
                    ontBonMaisTropTardQ2.append(message.author.id)

            else:
                await message.channel.send('Désolé vous avez perdu') 
                perduAnImporteQuelQ.append(message.author.id)

        # Dans le channel général et si c'est moi/Augustin bientôt        
        # elif message.author.id == myAuthorId:
        elif message.author.name == 'AMINE AA':
            print("Mon message dans le channel général :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS UP SIGN}') 
        #Si ce n'est pas le bot
        elif not isinstance(message.channel, discord.DMChannel) and message.author.id ==BOTman_id:
            print("Message du BOT dans le channel général :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS UP SIGN}')
        
        # Dans le channel et si c'est n'importe qui autre que moi
        elif not isinstance(message.channel, discord.DMChannel):
            print("Message par qq d'autres du channel :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS DOWN SIGN}')
        # Message du Bot     
        elif message.author.id == BOTman_id:
            print("Message du bot :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS UP SIGN}') 
        #si channel n'est le channel du prof/le mien par Augustin
        elif message.channel.id != my_channel_id:
            return
        # Tous les autres cas
        else:
            print("Tous les autres cas :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS DOWN SIGN}')
    except (RuntimeError):
        print("Une erreur est survenue...Fermeture")
        sys.exit(1)        

client.run('Tok')
