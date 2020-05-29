#!/usr/bin/env python3
# -- coding: utf-8 --
#4may , 5 may , 6 may commencé vers 18H20 , 7 may , 11 may , 12 may , 13 may, and 14 may, 15 may and 18 may,19may,21may,  25 may,27, 29 may
#sort added for podiumglobal and added !podium x, podiumsave dans challenge!!
import sys
import discord
from discord.ext import commands
from operator import itemgetter
import asyncio

tok = open("token.txt", "r")
token=tok.readlines()

my_channel_id = 705073195077730344

BOTman_id = 705418360216748062

myAuthorId = 476338851871326219
brice_Id=689134480291528710
admin_Id=480045172630224916

poder=0 #pour empêcher que si on tape Podium!! cela modifie le score
# e=0# 

top10NamesQall=[]
ontBonMaisTropTardQall=[]
perduAnImporteQuelQall=[]
perduAnImporteQuelQ = []
#variable
current_challenge=0

####
# Events
####
client = commands.Bot(command_prefix='.')

# #challenge rép
# rep1='1) Linux Mint'
# rep2='2) Google Images -> Insérer image -> Rechercher'
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

#init variable global podium
o=1#cbeme
totdico={}
# mondico={}
# q=10#score
# p=0#indice

#définition des fonctions
def init_list():
    global top10NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY
    top10NamesQY = []
    ontBonMaisTropTardQY = []
    perduAnImporteQuelQY = []

def fini_challenge(top10NamesQY,ontBonMaisTropTardQY, perduAnImporteQuelQY):
    top10NamesQall.append(top10NamesQY)
    ontBonMaisTropTardQall.append(ontBonMaisTropTardQY)
    perduAnImporteQuelQall.append(perduAnImporteQuelQY)

# def podium_user_mini():
#     global challengeprec
#     if current_challenge>1:
#         challengeprec=current_challenge-2
#         print('chall',challengeprec)
#         print("nbQxallgagnantx, top10NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
#         print(len(top10NamesQall), top10NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
# def list_player_for_score():
#     global e
#     e=0
#     for x in top10NamesQY: 
#         top10NamesQY[e]=[]

# def score():
#     global j,x,i
#     j=1#cbeme
#     x=0#indice
#     i=10#score
#     try:
#         while i<=10 and j<=10 and x<10:
#             print('x=',x)
#             print('j=',j)
#             print('i=',i)
#             mondico[x]=i
#             print('utilisateur '+ top10NamesQY[x]+ ' Top '+j+ ' a '+i+ ' points' )
#             i-=1
#             j+=1
#             x+=1
#     except (IndexError):
#         print("Impossible de trouver l'élément dans la liste")

def reptricheur(top10NamesQx, repx,  msg):
    if msg.author.name in top10NamesQx and msg.content.casefold()== repx.casefold() :
        print(reptriche1)
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
    global quest, rep, listchallengeq, listchallenger
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

def podiumsave():
    global totdico, top10NamesQY
    i=10
    x=0
    print('top10NameQY=', top10NamesQY)
    for s in top10NamesQY:
        print ('current_challenge!', current_challenge)
        if current_challenge > 1: 
            try: 
                totdico[top10NamesQY[x]]+=i
                x+=1
                i-=1
            except KeyError:
                totdico[top10NamesQY[x]]=i
                x+=1
                i-=1

        elif current_challenge == 1:
            totdico[top10NamesQY[x]]=i
            x+=1
            i-=1
        else:
            print('fini')
    return totdico
                    
@client.event
async def on_ready():
    print ('Challenge Bot est prêt.')
    return True        

@client.event
async def on_message(message):
    try:
        # global appel_membre, appel, absents, presents
        # global e
        # global o,q,p
        global o
        global top10NamesQall, ontBonMaisTropTardQall, perduAnImporteQuelQall, poder
        global j,x,i
        global current_challenge, totdico, top10NamesQY

        if message.author.id != BOTman_id:
            print("Je suis", message.author.name)
            print("Actuellement les valeurs sont :")
            print("my_channel_id, BOTman_id, myAuthorId", \
                my_channel_id, BOTman_id, myAuthorId)
            
            print("Message initial", message)
        # if message.content == 'Podium!!' \
        #     and message.author.id in (myAuthorId, 689134480291528710, 480045172630224916) :
        #     poder+=1
        # if message.content == 'Podium!!' \
        #     and message.author.id in (myAuthorId, 689134480291528710, 480045172630224916,BOTman_id) :
        #     # score()
        #     # j=1#cbeme
        #     # x=0#indice
        #     # i=10#score
        #     try:
        #             podiumsave()
        #             while poder>0:
        #                 totdico[top10NamesQY[p]]-=i
        #                 x+=1
        #                 # i-=1
        #                 poder-=1
        #             await message.channel.send('Gagnant tot= '+str(totdico))
        #             # await message.channel.send('utilisateur '+ top10NamesQY[x]+ ' Top '+str(j)+ ' a '+str(i)+ ' points' )
        #             # i-=1
        #             print('totdico', totdico)
        #     except (IndexError):
        #         print (" fini")#Impossible de trouver l'élément dans la liste

        if message.content == 'Podium!!!' \
            and message.author.id in (myAuthorId, 689134480291528710, 480045172630224916,BOTman_id) : #current_podiums
            # score()
            j=1#cbeme
            x=0#indice
            i=10#score
            try:
                while i<=10 and j<=10 and x<10:
                    await message.channel.send('utilisateur '+ top10NamesQY[x]+ ' Top '+str(j)+ ' a '+str(i)+ ' points' )
                    i-=1
                    j+=1
                    x+=1
            except (IndexError):
                await message.channel.send("Personne d'autres a gagné")#Impossible de trouver l'élément dans la liste
        if message.content == 'PodiumGlobal!!' \
            and message.author.id in (myAuthorId, 689134480291528710, 480045172630224916) : #podium global par les admins
            # list_player_for_score()
            try:
            #   print('zedico', totdico)
             o=1
             while o<=len(totdico):
                for cle, valeur in sorted(totdico.items(), key=itemgetter(1), reverse=True): #itemgetter 1 car on trie par rapport au score, reverse true trier a>b
                        print('utilisateur {}'.format(cle)+ ' Top '+str(o)+ ' a '+ '{} points'.format(valeur) )
                        await message.channel.send('utilisateur {}'.format(cle)+ ' Top '+str(o)+ ' a '+ '{} points'.format(valeur) )
                        o+=1
            except (IndexError):
                await message.channel.send("Personne d'autres a gagné")#Impossible de trouver l'élément dans la liste

        if message.content.casefold() == '!!podium'.casefold() :
            # score()
            j=1#cbeme
            x=0#indice
            i=10#score
            try:
                if current_challenge>1:
                    challengeprec=current_challenge-2
                    print('chall',challengeprec)
                    print("nbQxallgagnantx, top10NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                    print(len(top10NamesQall), top10NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
                while i<=10 and j<=10 and x<10:
                    print('x=',x)
                    print('j=',j)
                    print('i=',i)
                    await message.channel.send('utilisateur '+ str(top10NamesQall[challengeprec][x])+ ' Top '+str(j)+ ' a '+str(i)+ ' points' )
                    i-=1
                    j+=1
                    x+=1
            except (IndexError):
                await message.channel.send("Personne d'autres a gagné")#Impossible de trouver l'élément dans la liste
    # Pour les personnes qui peuvent lancer le Challenge
        if message.content == 'Challenge!!' \
            and message.author.id in (myAuthorId, 689134480291528710, 480045172630224916) :
            if (current_challenge>=1):
                fini_challenge(top10NamesQY,ontBonMaisTropTardQY, perduAnImporteQuelQY)

            if current_challenge== 0:
                init_list()
            fichreaderq1()
            
            await message.channel.send(listchallengeq[current_challenge])
            await message.channel.send('Réponse sous la forme : en MP')
            if current_challenge>0:
                try:
                    podiumsave()
                    # while poder>0:
                    #     totdico[top10NamesQY[p]]-=i
                    #     x+=1
                    #     poder-=1
                    await message.channel.send('Gagnant tot= '+str(totdico))
                    print('totdico', totdico)
                    print("top10NamesQY!!",top10NamesQY)
                except (IndexError):
                    print (" fini")#Impossible de trouver l'élément dans la liste
            current_challenge+=1
            init_list()
            if current_challenge==1:
                await message.channel.send('Si non faites un reverse search sur Google ou BING ')
                await message.channel.send('1) Google Chrome //ne pas oublier le numéro la parenthèse et l espace ')
            elif current_challenge==2:
                await message.channel.send('2) Google Chrome -> Téléchargement -> Cliquer sur le fichier téléchargé //ne pas oublier le numéro la parenthèse et l espace')
            else :
                await message.channel.send('3) Google Chrome //ne pas oublier le numéro la parenthèse et l espace ')

        if message.content == 'help!!':
            await message.channel.send('```!!podium affiche le podium précédent pour tous les utilisateurs```')
            await message.channel.send('```!podium x affiche le podium en fonction du numéro x précédent pour tous les utilisateurs```')
            await message.channel.send("```PodiumGlobal!! affiche le podium Global des challenges terminés destinés aux profs```")
            await message.channel.send('```Challenge!! lancer le challenge ou passer le challenge admin/prof```')
            await message.channel.send('```Podium!!! voir le podium du challenge actuel pour les admin/prof```')
            # await message.channel.send("```Podium!! destiné à forcer l'actualisation du bot destiné aux bots```")

        #afficher le podium du challenge terminé que l'on souhaite voir
        if message.content.startswith('!podium'):
            typed=message.content
            delimited=typed.split(' ') 
            podiuming=delimited[0]
            numberpodiuming=delimited[1]
            numberpodium= int(numberpodiuming)
            # print("message= "+ message.content)
            # print("podiuming= "+ podiuming)
            # print("numberpodium= "+numberpodiuming)
            # await message.channel.send('Say hello!')
            f=1#cbeme
            g=0#indice
            h=10#score
            try:
                if current_challenge>numberpodium:
                    # print("current_challenge=",current_challenge)
                    # challengeprec=current_challenge-2
                    # challengeprec=int(numberpodium)+1
                    challengeprec=numberpodium-1
                    print('chall',challengeprec)
                    print("nbQxallgagnantx, top10NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                    print(len(top10NamesQall), top10NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
                elif current_challenge==numberpodium:
                    await message.channel.send("Ce challenge est en cours !! Veuillez attendre qu'il soit terminé !")
                else: 
                   await message.channel.send("Ce challenge n'a pas démarré!!")
                while h<=10 and f<=10 and g<10:
                    print('g=',g)
                    print('f=',f)
                    print('h=',h)
                    await message.channel.send('utilisateur '+ str(top10NamesQall[challengeprec][g])+ ' Top '+str(f)+ ' a '+str(h)+ ' points' )
                    h-=1
                    f+=1
                    g+=1
            except (IndexError):
                await message.channel.send("Personne d'autres a gagné")#Impossible de trouver l'élément dans la liste
        
        # Dans le channel privée et si ce n'est pas le bot
        if isinstance(message.channel, discord.DMChannel) and message.author.id != BOTman_id :
            print("Message privé : " + message.content)
            fichreaderq1()
            listchallengerx=listchallenger[current_challenge-1]
            print("nbQxgagnant, top10NamesQY, ontBonMaisTropTardQY,  perduAnImporteQuelQY")
            print(len(top10NamesQY), top10NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY)
            if current_challenge>1:
                print("nbQxallgagnant, top10NamesQall, ontBonMaisTropTardQall,  perduAnImporteQuelQall")
                print(len(top10NamesQall), top10NamesQall, ontBonMaisTropTardQall, perduAnImporteQuelQall)
                challengeprec=current_challenge-2
                print('chall',challengeprec)
                print("nbQxallgagnantx, top10NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                print(len(top10NamesQall), top10NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
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
            
            if message.content.casefold()==listchallengerx.casefold() and reptricheur(top10NamesQY, listchallengerx, message)!=True :
                await message.channel.send(homer)      

            else:
                await message.channel.send('Désolé vous avez perdu') 
                perduAnImporteQuelQY.append(message.author.name)

            print("nbQxgagnant, top10NamesQY, ontBonMaisTropTardQY,  perduAnImporteQuelQY", "totdico")
            print(len(top10NamesQY), top10NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY, totdico)

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