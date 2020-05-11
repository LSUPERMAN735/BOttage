#!/usr/bin/env python3
# -- coding: utf-8 --
#4may and 5 may and 6 may commencé vers 18H20 and 7 may and 11 may
import sys
import discord
from discord.ext import commands
import asyncio

tok = open("token.txt", "r")
token=tok.readlines()

my_channel_id = 705073195077730344

BOTman_id = 705418360216748062

myAuthorId = 476338851871326219
brice_Id=689134480291528710
admin_Id=480045172630224916

top10IdsQ1 = []
top10IdsQ2 = []
# nbQ1Wins = len(top10IdsQ1)
# nbQ2Wins = len(top10IdsQ2) #ne fonctionne pas
ontBonMaisTropTardQ1 = []
ontBonMaisTropTardQ2 = []
perduAnImporteQuelQ = []
#variable
current_challenge=0
####
# Events
####
client = commands.Bot(command_prefix='.')

#challenge rép
rep1='1) Linux Mint'
rep2='2) Google Images -> Insérer image -> Rechercher'
#reponse du bot
msggagne='Vous avez gagné à la question'
#réponse bot
homer='Homer: Woohoo!! Vous êtes trop fort!!'
# rep triche:
reptriche1='Vous avez déjà participé ! Faîtes autre chose !!'
reptriche2='tente de tricher!!'

#reponse si trop tard du bot
repbotlate1='Désolé mais 10 autres personnes ont déjà gagné'
repbotlate1bis='Soyez plus rapide à la prochaine question '

#définition des fonctions
def reptricheur(top10IdsQx, repx,  msg):
    if msg.author.id in top10IdsQx and msg.content.casefold()== repx.casefold() :
        msg.channel.send(reptriche1)
        print(msg.author.id, reptriche2)
        return False# valeur qui bloque la questionx si l'utilisateur tente de rerépondre bon
    else: 
        return True

        #casefold pour ignorer la casse majuscule, minuscule ou mélangées
def repondre_quest(msg, repx, top10IdsQx, ontBonMaisTropTardQx, Qx):
    if msg.content.casefold() ==repx.casefold() and reptricheur(top10IdsQx, repx, msg)==True:
        # await msg.channel.send(gagnepremiereq)
        print(msggagne,Qx)
        print(msg.author.id)
        top10IdsQx.append(msg.author.id)
        print('gagné', Qx, '=', len(top10IdsQx))
        print('gagné', Qx, 'mais late =', len(ontBonMaisTropTardQx))
        return True

def fichreaderq1():        
    global quest, a, rep, listchallengeq, listchallenger
    fichdeqr = open("myq.txt", "r")
    lignes = fichdeqr.readlines()
    listchallengeq=[]
    listchallenger=[]
    for q in lignes :
        delims=q.split('|') 
        quest=delims[0]
        listchallengeq.append(quest)
        rep=delims[1]
        listchallenger.append(rep)
        
    fichdeqr.close()
    return quest,rep

# def fichreaderq2plus():
#     global questx, b, repx
#     fichdeqr = open("myq.txt", "r")
#     lignes = fichdeqr.readlines()
#     b=0
#     i=2
#     for q in lignes :
#         b+=1
#         delims=q.split('|') 
#         print('b=',b)
#         if b>i-1 and b<=i :
#             # i+=1
#             questx=delims[0]
#             repx=delims[1]
#     fichdeqr.close()
#     return questx,repx
                    
@client.event
async def on_ready():
    print ('Challenge Bot est prêt.')
    return True        

@client.event
async def on_message(message):
    try:
        # global appel_membre, appel, absents, presents
        # global quest2, rep2, b
        # global quest,a, rep, quest2, rep2, b
        global current_challenge
        global nbQ1gagnant, nbQ2gagnant, top10IdsQ1, top10IdsQ2, ontBonMaisTropTardQ1, ontBonMaisTropTardQ2, perduAnImporteQuelQ
        if message.author.id != BOTman_id:
            print("Je suis", message.author.id)
            print("Actuellement les valeurs sont :")
            print("my_channel_id, BOTman_id, myAuthorId", \
                my_channel_id, BOTman_id, myAuthorId)
            print("nbQ1gagnant, nbQ2gagnant, top10IdsQ1,top10IdsQ2, ontBonMaisTropTardQ1, ontBonMaisTropTardQ2, perduAnImporteQuelQ")
            print(len(top10IdsQ1), len(top10IdsQ2), top10IdsQ1, top10IdsQ2, ontBonMaisTropTardQ1, ontBonMaisTropTardQ2, perduAnImporteQuelQ)
            print("Message initial", message)
        
        # Pour les personnes qui peuvent lancer le Challenge
        if message.content == 'Challenge!!' \
            and message.author.id in (myAuthorId, 689134480291528710, 480045172630224916) :
            # fichdeqr = open("myq.txt", "r")
            # lignes = fichdeqr.readlines()
            # a=0
            # for q in lignes :
            #     a+=1
            #     delims=q.split('|')
            #     quest=delims[0]
            #     rep=delims[1]
            #     if a<=1 :
            fichreaderq1()
            await message.channel.send(listchallengeq[current_challenge])
            await message.channel.send('Si non faites un reverse search sur Google ou BING ')
            await message.channel.send('Réponse sous la forme : en MP')
            await message.channel.send('1) Google Chrome //ne pas oublier le numéro la parenthèse et l espace et majuscule')
            current_challenge+=1
            await message.channel.send('2) Google Chrome -> Téléchargement -> Cliquer sur le fichier téléchargé //ne pas oublier le numéro la parenthèse et l espace et majuscule')
            # fichdeqr.close()
        # elif message.content == '!!Challenge' \
        #     and message.author.id in (myAuthorId, 689134480291528710, 480045172630224916) :  
            # fichdeqr = open("myq.txt", "r")
            # lignes = fichdeqr.readlines()
            # b=0
            # for q in lignes :
            #     b+=1  
            #     delims=q.split('|')
            #     if b>1 and b<=2 :
            #         quest2=delims[0]
            #         rep2=delims[1]
            # fichreaderq2plus()
            # await message.channel.send(questx)  
            # await message.channel.send('Challenge 2 : Comment faire le reverse search ?')
            # await message.channel.send('Réponse sous la forme : en MP')
            # await message.channel.send('2) Google Chrome -> Téléchargement -> Cliquer sur le fichier téléchargé //ne pas oublier le numéro la parenthèse et l espace et majuscule')
            # fichdeqr.close()

        # Dans le channel privée et si ce n'est pas le bot
        if isinstance(message.channel, discord.DMChannel) and message.author.id != BOTman_id :
            print("Message privé : " + message.content)
            
            if reptricheur(top10IdsQ1, rep1, message)!=True:
                await message.channel.send(reptriche1) 
            if repondre_quest(message, rep1, top10IdsQ1, ontBonMaisTropTardQ1,'Q1') == True :
                await message.channel.send(msggagne+' 1')
                
            if len(top10IdsQ1) > 10:
                await message.channel.send(repbotlate1)
                await message.channel.send(repbotlate1bis)
                ontBonMaisTropTardQ1.append(message.author.id)#sinon bug

            if message.content.casefold()==rep1.casefold() and reptricheur(top10IdsQ1, rep1,  message)!=True :#casefold pour ignorer la casse majuscule, minuscule ou mélangées
                await message.channel.send(homer) 

            elif reptricheur(top10IdsQ2, rep2, message)!=True:
                await message.channel.send(reptriche1) 
            elif repondre_quest(message, rep2, top10IdsQ2, ontBonMaisTropTardQ2,'Q2') == True :
                await message.channel.send(msggagne+' 2')
                
                if len(top10IdsQ2) > 10:
                    await message.channel.send(repbotlate1)
                    await message.channel.send(repbotlate1bis)
                    ontBonMaisTropTardQ2.append(message.author.id) #sinon bug
                
                if message.content.casefold()==rep2.casefold() and reptricheur(top10IdsQ2, rep2, message)!=True :
                    await message.channel.send(homer) 
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

client.run(token[0])
