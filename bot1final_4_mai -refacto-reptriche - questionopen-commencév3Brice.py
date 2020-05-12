#!/usr/bin/env python3
# -- coding: utf-8 --
#4may and 5 may and 6 may commencé vers 18H20 and 7 may and 11 may and 12 may
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

top10NamesQ1 = []
top10NamesQ2 = []
# nbQ1Wins = len(top10NamesQ1)
# nbQ2Wins = len(top10NamesQ2) #ne fonctionne pas
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
def init_list():
    global top10NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY
    top10NamesQY = []
    ontBonMaisTropTardQY = []
    perduAnImporteQuelQY = []

def fini_challenge(top10NamesQY,ontBonMaisTropTardQY, perduAnImporteQuelQY):
    global top10NamesQall, ontBonMaisTropTardQall, perduAnImporteQuelQall
    top10NamesQall=[]
    ontBonMaisTropTardQall=[]
    perduAnImporteQuelQall=[]
    top10NamesQall.append(top10NamesQY)
    ontBonMaisTropTardQall.append(ontBonMaisTropTardQY)
    perduAnImporteQuelQall.append(perduAnImporteQuelQY)
def reptricheur(top10NamesQx, repx,  msg):
    if msg.author.name in top10NamesQx and msg.content.casefold()== repx.casefold() :
        msg.channel.send(reptriche1)
        print(msg.author.name, reptriche2)
        return False# valeur qui bloque la questionx si l'utilisateur tente de rerépondre bon
    else: 
        return True

        #casefold pour ignorer la casse majuscule, minuscule ou mélangées
def repondre_quest(msg, repx, top10NamesQx, ontBonMaisTropTardQx, Qx):
    if msg.content.casefold() ==repx.casefold() and reptricheur(top10NamesQx, repx, msg)==True:
        print(msggagne,Qx)
        print(msg.author.name)
        top10NamesQx.append(msg.author.name)
        print('gagné', Qx, '=', len(top10NamesQx))
        print('gagné', Qx, 'mais late =', len(ontBonMaisTropTardQx))
        return True

def fichreaderq1():        
    global quest, a, rep, listchallengeq, listchallenger
    fichdeqr = open("myq.txt", "r")
    lignes = fichdeqr.readlines()
    listchallengeq=[]
    listchallenger=[]
    for q in lignes :
        q= q.rstrip()
        delims=q.split('|') 
        quest=delims[0]
        listchallengeq.append(quest)
        rep=delims[1]
        listchallenger.append(rep)
    fichdeqr.close()
    return quest,rep

                    
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
        global nbQ1gagnant, nbQ2gagnant, top10NamesQ1, top10NamesQ2, ontBonMaisTropTardQ1, ontBonMaisTropTardQ2, perduAnImporteQuelQ
        if message.author.id != BOTman_id:
            print("Je suis", message.author.name)
            print("Actuellement les valeurs sont :")
            print("my_channel_id, BOTman_id, myAuthorId", \
                my_channel_id, BOTman_id, myAuthorId)
            # print("nbQ1gagnant, nbQ2gagnant, top10NamesQ1,top10NamesQ2, ontBonMaisTropTardQ1, ontBonMaisTropTardQ2, perduAnImporteQuelQ")
            # print(len(top10NamesQ1), len(top10NamesQ2), top10NamesQ1, top10NamesQ2, ontBonMaisTropTardQ1, ontBonMaisTropTardQ2, perduAnImporteQuelQ)
            
            print("Message initial", message)
        
        # Pour les personnes qui peuvent lancer le Challenge
        if message.content == 'Challenge!!' \
            and message.author.id in (myAuthorId, 689134480291528710, 480045172630224916) :
           
            if (current_challenge>=1):
                fini_challenge(top10NamesQY,ontBonMaisTropTardQY, perduAnImporteQuelQY)
           
            init_list()
            fichreaderq1()
            
            await message.channel.send(listchallengeq[current_challenge])
            await message.channel.send('Réponse sous la forme : en MP')
            current_challenge+=1
            if current_challenge==1:
                await message.channel.send('Si non faites un reverse search sur Google ou BING ')
                await message.channel.send('1) Google Chrome //ne pas oublier le numéro la parenthèse et l espace ')
            elif current_challenge==2:
                await message.channel.send('2) Google Chrome -> Téléchargement -> Cliquer sur le fichier téléchargé //ne pas oublier le numéro la parenthèse et l espace')
            else :
                await message.channel.send('3) Google Chrome //ne pas oublier le numéro la parenthèse et l espace ')


        # Dans le channel privée et si ce n'est pas le bot
        if isinstance(message.channel, discord.DMChannel) and message.author.id != BOTman_id :
            print("Message privé : " + message.content)
            fichreaderq1()
            listchallengerx=listchallenger[current_challenge-1]
            # init_list(top10IdsQ+[current_challenge],ontBonMaisTropTardQ, perduAnImporteQuelQY+[current_challenge])
            # init_list(top10IdsQ3,ontBonMaisTropTardQ3, perduAnImporteQuelQ3)
            print("nbQxgagnant, top10NamesQY, ontBonMaisTropTardQY,  perduAnImporteQuelQY")
            print(len(top10NamesQY), top10NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY)
            if current_challenge>1:
                print("nbQxallgagnant, top10NamesQall, ontBonMaisTropTardQall,  perduAnImporteQuelQall")
                print(len(top10NamesQall), top10NamesQall, ontBonMaisTropTardQall, perduAnImporteQuelQall)
                print("nbQxallgagnantx, top10NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                print(len(top10NamesQall), top10NamesQall[1], ontBonMaisTropTardQall[0], perduAnImporteQuelQall[1])
            print('message utilisateur=', message.content)
            # print('réponse=', listchallengerx)
            if reptricheur(top10NamesQY, listchallengerx, message)!=True:
                await message.channel.send(reptriche1) 
            
            if repondre_quest(message, listchallengerx, top10NamesQY, ontBonMaisTropTardQY,'Q'+str(current_challenge)) == True :
                await message.channel.send(msggagne+str(current_challenge))             
            
            if len(top10NamesQY) > 10:
                await message.channel.send(repbotlate1)
                await message.channel.send(repbotlate1bis)
                ontBonMaisTropTardQY.append(message.author.name) #sinon bug
            # if message.content.casefold()==rep1.casefold() and reptricheur(top10NamesQ1, rep1,  message)!=True :#casefold pour ignorer la casse majuscule, minuscule ou mélangées
            #     await message.channel.send(homer) 
            
            if message.content.casefold()==listchallengerx.casefold() and reptricheur(top10NamesQY, listchallengerx, message)!=True :
                await message.channel.send(homer)      

            else:
                await message.channel.send('Désolé vous avez perdu') 
                perduAnImporteQuelQY.append(message.author.name)

        # Dans le channel général et si c'est moi/Augustin bientôt        
        # elif message.author.name == myAuthorId:
        elif message.author.name == 'AMINE AA':
            print("Mon message dans le channel général :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS UP SIGN}') 
        #Si ce n'est pas le bot
        elif not isinstance(message.channel, discord.DMChannel) and message.author.id == BOTman_id:
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
