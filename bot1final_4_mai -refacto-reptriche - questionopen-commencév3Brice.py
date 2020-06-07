#!/usr/bin/env python3
# -- coding: utf-8 --
#4may , 5 may , 6 may commencé vers 18H20 , 7 may , 11 may , 12 may , 13 may, and 14 may, 15 may and 18 may,19may,21may,  25 may,27, 29 may,5juin,6juin,7juin
#sort added for podiumglobal and added !podium x, podiumsave dans challenge!!
import sys
import discord
from discord.ext import commands
from operator import itemgetter
import asyncio

tok = open("token.txt", "r")
token=tok.readlines()

my_channel_id = 705073195077730344
my_channel_id2 = 706529394318901328
my_channel_id3 = 706529394318901331

BOTman_id = 705418360216748062

myAuthorId = 476338851871326219
brice_Id=68913448029152873
brice_identifiant=689134480291528710
admin_Id=480045172630224916

# poder=0 #pour empêcher que si on tape Podium!! cela modifie le score
# e=0# 

top3NamesQall=[]
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
msggagne='Vous avez bon à la question'
#réponse bot
homer='Homer: Woohoo!! Vous êtes trop fort!!'
# rep triche:
reptriche1='Vous avez déjà participé ! Faîtes autre chose !!'
reptriche2='tente de tricher!!'

#reponse si trop tard du bot
repbotlate1='Mais 3 autres personnes ont déjà gagné, vous êtes trop lent donc 0 point '
repbotlate1bis='Soyez plus rapide à la prochaine question '

#init variable global podium
o=1#cbeme
totdico={}

# mondico={}
# q=3#score
# p=0#indice

#définition des fonctions
def init_od_totidcoinc_totdicoincrease():
    global bomdiggybombom, od, totdicoinc, totdicoincrease
    bomdiggybombom=0#empeche une réexucution de la boucle bug bizarre
    od=0
    totdicoinc=0 
    totdicoincrease=0
def init_var_score():
    global j, x, i 
    j=1#cbeme
    x=0#indice
    i=3#score
def init_f_g_h():
    global f, g, h
    f=1#cbeme
    g=0#indice
    h=3#score
def init_list():
    global top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY
    top3NamesQY = []
    ontBonMaisTropTardQY = []
    perduAnImporteQuelQY = []

def fini_challenge(top3NamesQY,ontBonMaisTropTardQY, perduAnImporteQuelQY):
    top3NamesQall.append(top3NamesQY)
    ontBonMaisTropTardQall.append(ontBonMaisTropTardQY)
    perduAnImporteQuelQall.append(perduAnImporteQuelQY)

# def podium_user_mini():
#     global challengeprec
#     if current_challenge>1:
#         challengeprec=current_challenge-2
#         print('chall',challengeprec)
#         print("nbQxallgagnantx, top3NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
#         print(len(top3NamesQall), top3NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
# def list_player_for_score():
#     global e
#     e=0
#     for x in top3NamesQY: 
#         top3NamesQY[e]=[]

# def score():
#     global j,x,i
#     j=1#cbeme
#     x=0#indice
#     i=3#score
#     try:
#         while i<=3 and j<=3 and x<3:
#             print('x=',x)
#             print('j=',j)
#             print('i=',i)
#             mondico[x]=i
#             print('utilisateur '+ top3NamesQY[x]+ ' Top '+j+ ' a '+i+ ' points' )
#             i-=1
#             j+=1
#             x+=1
#     except (IndexError):
#         print("Impossible de trouver l'élément dans la liste")

def reptricheur(top3NamesQx, repx,  msg):
    if msg.author.name in top3NamesQx and msg.content.casefold()== repx.casefold() :
        print(reptriche1)
        print(msg.author.name, reptriche2)
        return False# valeur qui bloque la questionx si l'utilisateur tente de rerépondre bon
    else: 
        return True

        #casefold pour ignorer la casse majuscule, minuscule ou mélangées
def repondre_quest(msg, repx, top3NamesQx, ontBonMaisTropTardQx, Qx):
    if msg.content.casefold() ==repx.casefold() and reptricheur(top3NamesQx, repx, msg)==True:
        print(msggagne,Qx)
        print(msg.author.name)
        top3NamesQx.append(msg.author.name)
        print('gagné', Qx, '=', len(top3NamesQx))
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
    global totdico, top3NamesQY
    i=3#score
    # x=0#indice
    print('top3NameQY=', top3NamesQY)
    for s in top3NamesQY:
        print ('current_challenge!', current_challenge)
        # if i<=0:#permet d'éviter un score négatif
        #     i=0#0 pour tous les gens en retard ou perdant
        if i > 0:
            if current_challenge > 1: 
                try: 
                    totdico[s]+=i
                    # x+=1
                    i-=1
                except KeyError:
                    totdico[s]=i
                    # x+=1
                    i-=1
                    print('exception')
            elif current_challenge == 1:
                totdico[s]=i
                # x+=1
                i-=1
            else:
                print('fini')
    return totdico

def podiumnum(message):
    global typed, delimited, podiuming, numberpodiuming, numberpodium
    typed=message.content
    delimited=typed.split(' ') 
    podiuming=delimited[0]
    numberpodiuming=delimited[1]
    numberpodium= int(numberpodiuming)
    print("message= "+ message.content)
    print("podiuming= "+ podiuming)
    print("numberpodium= "+numberpodiuming)
    return typed, delimited, podiuming, numberpodiuming, numberpodium
# def fact_malus(bomdiggybombom, od, totdicoinc, totdicoincrease, message_author_name, totdico):#bug refcato
    #  while od<=len(totdico) :
    #             # for cle, valeur in sorted(totdico.items(), key=itemgetter(1), reverse=True): #itemgetter 1 car on trie par rapport au score, reverse true trier a>b
    #             for cle, valeur in totdico.items() : #itemgetter 1 car on trie par rapport au score, reverse true trier a>b
    #                 # print('im here')
    #                 # print ('cle', cle)
    #                 # print ('valeur', valeur)
    #                 # print ('msg.author.name', message_author_name)
    #                 if cle == message_author_name and bomdiggybombom == 0 and totdicoincrease==0 :
    #                     # print("we are here")
    #                     # print(totdico[0])
    #                     # print(totdico[1])
    #                     # print(totdico[cle])
    #                     # print(totdico[2])#br
    #                     # print(totdico[3])#à tester
    #                     totdico[cle]-=2# 2 points de malus pour non respect des consignes ou totdico[cle]=valeur-2
    #                     # totdico[cle]-=-2# 2 points de malus pour non respect des consignes#-1 pour 3 fait indice-2
    #                     bomdiggybombom+=1
    #                     print('bomdiggybombom')
    #                 else :
    #                     # totdico[message.author.name]=0#RuntimeError: dictionary changed size during iteration
    #                     totdicoinc+=1#RuntimeError: dictionary changed size during iteration
    #                     # totdico[message.author.name]-=2
    #             od+=1
                #cette partie bug en refacto ci-dessous
    #             if totdicoinc == 1 and bomdiggybombom == 0 :# si l'utilisateur n'est pas dans totdico la boucle s'exécute parfois même si l'user y est d'où le bomdiggy
    #                 print("im 367")
    #                 totdico[message.author.name]=0#RuntimeError: dictionary changed size during iteration
    #                 totdico[message.author.name]-=2
    #                 totdicoincrease+=1          
@client.event
async def on_ready():
    print ('Challenge Bot est prêt.')
    # await message.channel.send('Coucou je suis BOTman')
    return True        

@client.event
async def on_message(message):
    try:
        # global appel_membre, appel, absents, presents
        # global e
        # global o,q,p
        global o
        global top3NamesQall, ontBonMaisTropTardQall, perduAnImporteQuelQall, poder
        global j,x,i
        global current_challenge, totdico, top3NamesQY
        global bomdiggybombom, od, totdicoinc, totdicoincrease
        global f, g, h

        if message.author.id != BOTman_id:
            print("Je suis", message.author.name)
            print("Actuellement les valeurs sont :")
            print("my_channel_id, BOTman_id, myAuthorId", \
                my_channel_id, BOTman_id, myAuthorId)
            
            print("Message initial", message)


        # if message.content == 'Podium!!' \
        #     and message.author.id in (myAuthorId, 68913448029152873, 480045172630224916) :
        #     poder+=1
        # if message.content == 'Podium!!' \
        #     and message.author.id in (myAuthorId, 68913448029152873, 480045172630224916,BOTman_id) :
        #     # score()
        #     # j=1#cbeme
        #     # x=0#indice
        #     # i=3#score
        #     try:
        #             podiumsave()
        #             while poder>0:
        #                 totdico[top3NamesQY[p]]-=i
        #                 x+=1
        #                 # i-=1
        #                 poder-=1
        #             await message.channel.send('Gagnant tot= '+str(totdico))
        #             # await message.channel.send('utilisateur '+ top3NamesQY[x]+ ' Top '+str(j)+ ' a '+str(i)+ ' points' )
        #             # i-=1
        #             print('totdico', totdico)
        #     except (IndexError):
        #         print (" fini")#Impossible de trouver l'élément dans la liste

        if message.content == 'Podium!!!' \
            and message.author.id in (myAuthorId, 689134480291528710, 480045172630224916,BOTman_id) : #current_podiums
            # score()
            init_var_score()   #j=cbeme, x=indice, i=score
            try:
                while i<=3 and j<=3 and x<3:
                    await message.channel.send(top3NamesQY[x]+ ' Top '+str(j)+ ' a '+str(i)+ ' points' )
                    i-=1
                    j+=1
                    x+=1
            except (IndexError):
                await message.channel.send("Personne d'autres a gagné")#Impossible de trouver l'élément dans la liste
        if message.content == 'PodiumGlobal!!' \
            and message.author.id in (myAuthorId, 68913448029152873, 480045172630224916) : #podium global par les admins
            # list_player_for_score()
            if current_challenge==1:
                await message.channel.send("Veuillez attendre que le challenge soit terminé ou faites Podium!!!")
            try:
                o=1
                while o<=len(totdico):
                    for cle, valeur in sorted(totdico.items(), key=itemgetter(1), reverse=True): #itemgetter 1 car on trie par rapport au score, reverse true trier a>b
                            # if valeur>0 : 
                        print('utilisateur {}'.format(cle)+ ' Top '+str(o)+ ' a '+ '{} points'.format(valeur) )
                        await message.channel.send('utilisateur {}'.format(cle)+ ' Top '+str(o)+ ' a '+ '{} points'.format(valeur) )
                        o+=1
            except (IndexError):
                await message.channel.send("Personne d'autres a gagné")#Impossible de trouver l'élément dans la liste

        if message.content.casefold() == '!!podium'.casefold() :
            # score()
            init_var_score() #j=cbeme, x=indice, i=score
            try:
                if current_challenge>1:
                    challengeprec=current_challenge-2
                    print('chall',challengeprec)
                    print("nbQxallgagnantx, top3NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                    print(len(top3NamesQall), top3NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
                while i<=3 and j<=3 and x<3:
                    print('x=',x)
                    print('j=',j)
                    print('i=',i)
                    await message.channel.send('utilisateur '+ str(top3NamesQall[challengeprec][x])+ ' Top '+str(j)+ ' a '+str(i)+ ' points' )
                    i-=1
                    j+=1
                    x+=1
            except (IndexError):
                await message.channel.send("Personne d'autres a gagné")#Impossible de trouver l'élément dans la liste
    # Pour les personnes qui peuvent lancer le Challenge
        if message.content == 'Challenge!!' \
            and message.author.id in (myAuthorId, 68913448029152873, 480045172630224916) :
            
            if (current_challenge>=1):
                fini_challenge(top3NamesQY,ontBonMaisTropTardQY, perduAnImporteQuelQY)

            if current_challenge== 0:
                init_list()
            fichreaderq1()
            
            if current_challenge==len(listchallengeq):
                fini_challenge(top3NamesQY,ontBonMaisTropTardQY, perduAnImporteQuelQY)
                podiumsave()
                await message.channel.send('Gagnant tot= '+str(totdico))
                await message.channel.send("Tous les challenges sont désormais terminés")
                current_challenge+=1

            await message.channel.send(listchallengeq[current_challenge])
            # await message.channel.send('Réponse sous la forme : en MP')
            if current_challenge>0:
                try:
                    podiumsave()
                    await message.channel.send('Gagnant tot= '+str(totdico))
                    print('totdico', totdico)
                    print("top3NamesQY!!",top3NamesQY)
                except (IndexError):
                    print (" fini")#Impossible de trouver l'élément dans la liste
            current_challenge+=1
            init_list()
            # if current_challenge==1:
                # await message.channel.send('Si non faites un reverse search sur Google ou BING ')
                # await message.channel.send('1) Google Chrome //ne pas oublier le numéro la parenthèse et l espace ')
            # elif current_challenge==2:
            #     # await message.channel.send('2) Google Chrome -> Téléchargement -> Cliquer sur le fichier téléchargé //ne pas oublier le numéro la parenthèse et l espace')
            # else :
            #     await message.channel.send('3) Google Chrome //ne pas oublier le numéro la parenthèse et l espace ')
        
        # if any(bad_word in message for bad_word in listchallenger):#TypeError: argument of type 'Message' is not iterab
        #     await bot.send_message(message.channel, "{}, your message has been censored.".format(message.author.mention))
        #     await bot.delete_message(message)
       
        # print('cr',current_challenge)
        print('listcr',listchallenger[current_challenge-1])
        if message.content == listchallenger[current_challenge-1] and message.channel.id == my_channel_id3 :
        # if message.content.casefold() == listchallenger[current_challenge].casefold() :
            
            print(message.content)
            await message.delete()#discord.errors.Forbidden: 403 Forbidden (error code: 50013): Missing Permissions
            await message.channel.send(message.author.name+" Vous devez saisir la réponse en message privée!!! \n -2Points ROHH!! ```Bart: Wohooh t'es trop ...```")
            print('i am here')
            init_od_totidcoinc_totdicoincrease()      
            #od pour parcourir le totdico #totdicoinc pour les gens qui n'existe pas dans totdico #totdicoincrease pour ne pas rentrer dans la boucle Clodomir
          
            print('bomdiggybombom', bomdiggybombom)
            # if current_challenge == 1 :
            #     # fini_challenge(top3NamesQY,ontBonMaisTropTardQY, perduAnImporteQuelQY)
            #     podiumsave()
            print('od', od)
            print('lentotdico', len(totdico))
            # print('current_challenge', current_challenge)
            # while od<=len(totdico) or current_challenge == 1:
            # while od<=len(totdico) or message.content == listchallenger[current_challenge-1] :#boucle infinie
            # while message.content == listchallenger[current_challenge-1] and current_challenge == 1 : #boucle infinie empeche de passer au challenge 2
            #boucle while Clodomir permet de retirer aux utilisateurs dans totdico les malus des gens qui répondent dans le channel
            # fact_malus(bomdiggybombom, od, totdicoinc, totdicoincrease, message.author.name, totdico)# bug avec refacto
            while od<=len(totdico) :
                # for cle, valeur in sorted(totdico.items(), key=itemgetter(1), reverse=True): #itemgetter 1 car on trie par rapport au score, reverse true trier a>b
                for cle, valeur in totdico.items() : #itemgetter 1 car on trie par rapport au score, reverse true trier a>b
                    # print('im here')
                    # print ('cle', cle)
                    # print ('valeur', valeur)
                    # print ('msg.author.name', message.author.name)
                    if cle == message.author.name and bomdiggybombom == 0 and totdicoincrease==0 :
                        # print("we are here")
                        # print(totdico[0])
                        # print(totdico[1])
                        # print(totdico[cle])
                        # print(totdico[2])#br
                        # print(totdico[3])#à tester
                        totdico[cle]-=2# 2 points de malus pour non respect des consignes ou totdico[cle]=valeur-2
                        # totdico[cle]-=-2# 2 points de malus pour non respect des consignes#-1 pour 3 fait indice-2
                        bomdiggybombom+=1
                        print('bomdiggybombom')
                    else :
                        # totdico[message.author.name]=0#RuntimeError: dictionary changed size during iteration
                        totdicoinc+=1#RuntimeError: dictionary changed size during iteration
                        # totdico[message.author.name]-=2
                od+=1
                if totdicoinc == 1 and bomdiggybombom == 0 :# si l'utilisateur n'est pas dans totdico la boucle s'exécute parfois même si l'user y est d'où le bomdiggy
                    print("im 367")
                    totdico[message.author.name]=0#RuntimeError: dictionary changed size during iteration
                    totdico[message.author.name]-=2
                    totdicoincrease+=1          
                    # totdicoinc=0
            # for elem in totdico: 
            #     print('s',elem)
            #     print('ttdico',totdico[elem])
            #     if totdico[elem] == message.author.name:
            #        print('doing')
                #    totdico[elem]-=2# 2 points de malus pour non respect des consignes
            # for s in top3NamesQY : 
                # print(s)
                # print(top3NamesQY[s])
                # if top3NamesQY[s] == message.author.name :
            # await client.delete_message(message)# AttributeError: 'Bot' object has no attribute 'delete_message' AttributeError: 'Bot' object has no attribute 'delete_messages'

        if message.content.casefold() == 'help!!'.casefold():
            await message.channel.send('```!!podium affiche le podium précédent pour tous les utilisateurs```'+\
                '```!podium x affiche le podium en fonction du numéro x précédent pour tous les utilisateurs```'\
                +"```PodiumGlobal!! affiche le podium Global des challenges terminés destinés aux profs```"+\
                '```Challenge!! lancer le challenge ou passer le challenge admin/prof```'+'```Podium!!! voir le podium du challenge actuel pour les admin/prof```')
            # await message.channel.send('```!podium x affiche le podium en fonction du numéro x précédent pour tous les utilisateurs```')
            # await message.channel.send("```PodiumGlobal!! affiche le podium Global des challenges terminés destinés aux profs```")
            # await message.channel.send('```Challenge!! lancer le challenge ou passer le challenge admin/prof```')
            # await message.channel.send('```Podium!!! voir le podium du challenge actuel pour les admin/prof```')
            # await message.channel.send("```Podium!! destiné à forcer l'actualisation du bot destiné aux bots```")

        #afficher le podium du challenge terminé que l'on souhaite voir
        if message.content.startswith('!podium'):
            podiumnum(message)
            init_f_g_h() # f=cbeme, g=indice, h=score
            try:
                    if current_challenge>numberpodium:
                        # print("current_challenge=",current_challenge)
                        # challengeprec=current_challenge-2
                        # challengeprec=int(numberpodium)+1
                        challengeprec=numberpodium-1
                        print('chall',challengeprec)
                        print("nbQxallgagnantx, top3NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                        print(len(top3NamesQall), top3NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
                    elif current_challenge==numberpodium:
                        await message.channel.send("Ce challenge est en cours !! Veuillez attendre qu'il soit terminé !")
                    else: 
                        await message.channel.send("Ce challenge n'a pas démarré!!")
                    while h<=3 and f<=3 and g<3:
                        print('g=',g)
                        print('f=',f)
                        print('h=',h)
                        await message.channel.send('utilisateur '+ str(top3NamesQall[challengeprec][g])+ ' Top '+str(f)+ ' a '+str(h)+ ' points' )
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
            print("nbQxgagnant, top3NamesQY, ontBonMaisTropTardQY,  perduAnImporteQuelQY")
            print(len(top3NamesQY), top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY)
            if current_challenge>1:
                print("nbQxallgagnant, top3NamesQall, ontBonMaisTropTardQall,  perduAnImporteQuelQall")
                print(len(top3NamesQall), top3NamesQall, ontBonMaisTropTardQall, perduAnImporteQuelQall)
                challengeprec=current_challenge-2
                print('chall',challengeprec)
                print("nbQxallgagnantx, top3NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                print(len(top3NamesQall), top3NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
            print('message utilisateur=', message.content)
            # print('réponse=', listchallengerx)
            if reptricheur(top3NamesQY, listchallengerx, message)!=True:
                await message.channel.send(reptriche1) 
            
            if repondre_quest(message, listchallengerx, top3NamesQY, ontBonMaisTropTardQY,'Q'+str(current_challenge)) == True :
                # await message.channel.send(msggagne+str(current_challenge))             
                await message.channel.send(msggagne+str(current_challenge)+"\n"+homer)             
                # await message.channel.send(homer)      
           
                perduAnImporteQuelQY.append(message.author.name)
            if len(top3NamesQY) > 3:
                await message.channel.send(repbotlate1)
                await message.channel.send(repbotlate1bis)
                ontBonMaisTropTardQY.append(message.author.name) #sinon bug si refacto
            
            if message.content.casefold()==listchallengerx.casefold() and reptricheur(top3NamesQY, listchallengerx, message)!=True :
            #     await message.channel.send(homer)      
                  truc=None#cette fonction sert à n'envoyer que si c'est la mauvaise réponseet ou l'utilisateur reparticipe
            elif message.author.name in top3NamesQY: # cette fonction permet de ne pas afficher de message au tricheur
                arretedeparticiper=None#arretedeparticiper bordel permet d'utiliser cette fonction
            else:
                await message.channel.send('Mauvaise réponse') 
                perduAnImporteQuelQY.append(message.author.name)

            print("nbQxgagnant, top3NamesQY, ontBonMaisTropTardQY,  perduAnImporteQuelQY", "totdico")
            print(len(top3NamesQY), top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY, totdico)

        # Dans le channel général et si c'est moi/Augustin bientôt        
        # elif message.author.name == myAuthorId:
        elif message.author.name == 'AMINE AA':
            print("Mon message dans le channel général :", message.content)
            # await message.add_reaction(emoji = '\N{THUMBS UP SIGN}') 
        #Si ce n'est pas le bot
        elif not isinstance(message.channel, discord.DMChannel) and message.author.id == BOTman_id:
            print("Message du BOT dans le channel général :", message.content)
            # await message.add_reaction(emoji = '\N{THUMBS UP SIGN}')

        # Dans le channel et si c'est n'importe qui autre que moi
        elif not isinstance(message.channel, discord.DMChannel):
            print("Message par qq d'autres du channel :", message.content)
            # await message.add_reaction(emoji = '\N{THUMBS DOWN SIGN}')
        # Message du Bot     
        elif message.author.id == BOTman_id:
            print("Message du bot :", message.content)
            # await message.add_reaction(emoji = '\N{THUMBS UP SIGN}') 
        #si channel n'est le channel du prof/le mien par Augustin
        elif message.channel.id != my_channel_id:
            return
        # Tous les autres cas
        else:
            print("Tous les autres cas :", message.content)
            # await message.add_reaction(emoji = '\N{THUMBS DOWN SIGN}')
    except (RuntimeError):
        print("Une erreur est survenue...Fermeture")
        sys.exit(1)        

client.run(token[0])