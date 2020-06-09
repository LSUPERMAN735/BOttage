#!/usr/bin/env python3
# -- coding: utf-8 --
#4may , 5 may , 6 may commencé vers 18H20 , 7 may , 11 may , 12 may , 13 may, and 14 may, 15 may and 18 may,19may,21may,  25 may,27, 29 may,5juin,6juin,7juin, 8juin, 9juin
#9juin
#sort added for podiumglobal and added !podium x, podiumsave dans challenge!!
#lisibility added
import sys
import discord
from discord.ext import commands
from operator import itemgetter
import asyncio

tok = open("token.txt", "r")
token = tok.readlines()

my_channel_id = 705073195077730344
my_channel_id2 = 706529394318901328
my_channel_id3 = 706529394318901331

BOTman_id = 705418360216748062

myAuthorId = 476338851871326219
brice_Id = 68913448029152873
brice_identifiant = 689134480291528710
admin_Id = 480045172630224916
clara_oswald = 718446180429725746

prof_grp_id = 690133601605386264
dev_grp_id = 719298857191604274
# poder=0 #pour empêcher que si on tape Podium!! cela modifie le score
# e=0# 

top3NamesQall = []
ontBonMaisTropTardQall = []
perduAnImporteQuelQall = []
perduAnImporteQuelQ = []
#variable
current_challenge = 0
exp_counter_podium = 0
help_counter = 0
podium_global_counter = 0
double_exp_podium_counter = 0
####
# Events
####
client = commands.Bot(command_prefix='.')

# #challenge rép -> fichier fichreaderq1() fini les brut

#réponse du bot
msggagne = 'Vous avez bon à la question'
#réponse bot
homer = 'Homer: Woohoo!! Vous êtes trop fort!!'
# rep triche:
reptriche1 = 'Vous avez déjà participé ! Faîtes autre chose !!'
reptriche2 = 'tente de tricher!!'

#reponse si trop tard du bot
repbotlate1 = 'Mais 3 autres personnes ont déjà gagné, vous êtes trop lent donc 0 point '
repbotlate1bis = 'Soyez plus rapide à la prochaine question '

#init variable global podium
o = 1#cbeme
totdico = {}
# mondico={}
# q=3#score
# p=0#indice

#définition des fonctions
# def init_od_totidcoinc_totdicoincrease() :
#     global bomdiggybombom, od, totdicoinc, totdicoincrease, boomboom
#     boomboom = 0
#     bomdiggybombom = 0#empêche une réexucution de la boucle bug bizarre
#     od = 0
#     totdicoinc = 0 
#     totdicoincrease = 0
# def init_var_score() :# *2 car comme ça si deux vlients envoie un message sur chaque salon différent ainsi les variables sont indépendants
#     global j, x, i 
#     j = 1#cbeme
#     x = 0#indice
#     i = 3#score
# def init_f_g_h() :
#     global f, g, h

def init_list() :
    global top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY
    top3NamesQY = []
    ontBonMaisTropTardQY = []
    perduAnImporteQuelQY = []

def fini_challenge(top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY) :
    top3NamesQall.append(top3NamesQY)
    ontBonMaisTropTardQall.append(ontBonMaisTropTardQY)
    perduAnImporteQuelQall.append(perduAnImporteQuelQY)


def reptricheur(top3NamesQx, repx,  msg) :
    if msg.author.name in top3NamesQx and msg.content.casefold() == repx.casefold() :
        print (reptriche1)
        print (msg.author.name, reptriche2)
        return False# valeur qui bloque la questionx si l'utilisateur tente de rerépondre bon
    else: 
        return True

        #casefold pour ignorer la casse majuscule, minuscule ou mélangées
def repondre_quest(msg, repx, top3NamesQx, ontBonMaisTropTardQx, Qx):
    if msg.content.casefold() == repx.casefold() and reptricheur(top3NamesQx, repx, msg) == True :
        print (msggagne,Qx)
        print (msg.author.name)
        top3NamesQx.append(msg.author.name)
        print ('gagné', Qx, '=', len(top3NamesQx))
        print ('gagné', Qx, 'mais late =', len(ontBonMaisTropTardQx))
        return True

def fichreaderq1() :
    global quest, rep, listchallengeq, listchallenger
    fichdeqr = open("myq.txt", "r")
    lignes = fichdeqr.readlines()
    listchallengeq = []
    listchallenger = []
    for q in lignes :
        q = q.rstrip()
        delims = q.split('|') 
        quest = delims[0]
        listchallengeq.append(quest)
        rep = delims[1]
        listchallenger.append(rep)
    fichdeqr.close()
    return quest, rep

def podiumsave(message_author_name) :
    global totdico, top3NamesQY
    i = 3#score
    # x=0#indice
    print ('top3NameQY=', top3NamesQY)
    for s in top3NamesQY :
        print ('current_challenge!', current_challenge)
        # if i<=0:#permet d'éviter un score négatif
        #     i=0#0 pour tous les gens en retard ou perdant
        if i > 0 : #permet de ne prendre que le top x avec point positif
            if current_challenge > 1 : 
                try: 
                    totdico[s] += i
                    # x+=1
                    i -= 1
                except KeyError :
                    totdico[s] = i
                    # x+=1
                    i -= 1
                    print ('exception')
            elif current_challenge == 1 and message_author_name not in totdico :
                totdico[s] = i
                # x+=1
                i -= 1
            elif current_challenge == 1 and message_author_name in totdico :
                totdico[s] += i
                i -= 1
            else :
                print ('fini')
    return totdico

def podiumnum(message) :
    global typed, delimited, podiuming, numberpodiuming, numberpodium
    typed = message.content
    delimited = typed.split(' ') 
    podiuming = delimited[0]
    numberpodiuming = delimited[1]
    numberpodium = int(numberpodiuming)
    print ("message= " + message.content)
    print ("podiuming= " + podiuming)
    print ("numberpodium= " + numberpodiuming)
    return typed, delimited, podiuming, numberpodiuming, numberpodium

def fact_malus(totdico, message_author_name) : # sert à retirer les points malus si réponse dans le salon sauf si challenge 1
            if message_author_name in totdico :
                totdico[message_author_name] -= 2
            else : 
                totdico[message_author_name] = -2
   
@client.event
async def on_ready() :
    print ('Challenge Bot est prêt.')
    # await message.channel.send('Coucou je suis BOTman')
    return True        

@client.event
async def on_message(message) :
    try:
        # global appel_membre, appel, absents, presents
        global exp_counter_podium, help_counter, double_exp_podium_counter, podium_global_counter
        global o
        global top3NamesQall, ontBonMaisTropTardQall, perduAnImporteQuelQall, poder
        global current_challenge, totdico, top3NamesQY
        
        if message.author.id != BOTman_id:
            print ("Je suis", message.author.name)
            print ("Actuellement les valeurs sont :")
            print ("my_channel_id, BOTman_id, myAuthorId", \
                my_channel_id, BOTman_id, myAuthorId)
            
            print ("Message initial", message)

        if message.content.casefold() == 'Podium!!!'.casefold() \
            and message.author.id in (myAuthorId, brice_identifiant, 480045172630224916) : #current_podiums
            f = 1#cbeme
            g = 0#indice
            h = 3#score
            try:
                while h <= 3 and f <= 3 and g < 3 :
                    await message.channel.send(top3NamesQY[g] + ' Top ' + str(f) + ' a ' + str(h) + ' points' )
                    h -= 1
                    f += 1
                    g += 1
            except (IndexError) :
                await message.channel.send("Personne d'autres a gagné")#Impossible de trouver l'élément dans la liste
                await message.channel.send(file=discord.File('./assets/done.gif'))

        
        if message.content.casefold() == 'PodiumGlobal!!'.casefold() :
            podium_global_counter += 1
            # print ('podium_global_counter', podium_global_counter)
            # and message.author.id in (myAuthorId, brice_identifiant, 480045172630224916, clara_oswald) : #podium global par les admins
            # and prof_grp_id in [y.id for y in Member(message.author).roles] or dev_grp_id in [y.id for y in Member(message.author).roles] : #podium global par les admins
            # and message.author.id in (myAuthorId, brice_identifiant, 480045172630224916) or prof_grp_id in [y.id for y in message.author.roles] or dev_grp_id in [y.id for y in message.author.roles] : #podium global par les admins
            # and message.author.id in (myAuthorId, brice_identifiant, 480045172630224916) or prof_grp_id in [y.id for y in message.author.roles] or dev_grp_id in [y.id for y in message.author.roles] : #podium global par les admins
            if current_challenge == 1 :
                await message.channel.send("Veuillez attendre que le challenge soit terminé ou faites Podium!!! si vous êtes prof")
      
            try :
                o = 1
                s=''
                for cle, valeur in sorted(totdico.items(), key = itemgetter(1), reverse = True): #itemgetter 1 car on trie par rapport au score, reverse true trier a>b
                    if valeur > 0 : #ne met ni d'erreur mais n'affiche pas que les valeurs supérieurs à 0
                        print('clé', cle)
                        print('valeur', valeur)
                        print ('utilisateur {}'.format(cle) +  ' Top ' + str(o) + ' a ' + '{} points'.format(valeur) )
                        await message.channel.send('utilisateur {}'.format(cle) + ' Top '+str(o) + ' a ' + '{} points'.format(valeur) )
                        s+='utilisateur' + str(cle) + ' Top ' + str(o) + ' a ' + str(valeur) + ' points' + '\n'
                        await message.channel.send(s)
                        o += 1

                if podium_global_counter in (1, 2, 7, 9, 14, 15, 21, 23, 31, 39, 41, 45, 50, 53, 55, 60, 65, 67, 78, 85) and message.author.id not in (brice_identifiant, brice_identifiant) :
                            if message.author.name in totdico and current_challenge > 1 :
                                # print(totdico[message.author.name])
                                totdico[message.author.name] += 2
                                await message.channel.send('Bravo à ' + message.author.name + ' BENDER : est allé vous cherchez 2 points bonus dans le FUTURama\
                                    \n c\'est bien de checker :)')
                                await message.channel.send(file=discord.File('./assets/bender.gif'))
                                if message.author.dm_channel == None : 
                                    help_message = 'l\'user ' + message.author.name + ' à gagner 2 pts avec podiumprec, current_challenge:'+ str(current_challenge)
                                    await message.author.create_dm()
                                    await message.author.send(str(help_message))    
                            elif message.author.name not in totdico and message.author.name not in top3NamesQY : 
                                totdico[message.author.name] = 2
                                await message.channel.send('Bravo à ' + message.author.name + ' BENDER : est allé vous cherchez vos 2 er points bonus dans le FUTURama\
                                    \n c\'est bien de checker')
                                await message.channel.send(file=discord.File('./assets/bender.gif'))
                                if message.author.dm_channel == None :
                                    help_message = 'l\'user ' + message.author.name + ' à gagner ses 3ers pts avec podiumprec, current_challenge:'+ str(current_challenge)
                                    await message.author.create_dm()
                                    await message.author.send(str(help_message))  
            except (IndexError) :
                await message.channel.send("Personne d'autres a gagné")#Impossible de trouver l'élément dans la liste

        if message.content.casefold() == '!!podium'.casefold() :
            double_exp_podium_counter += 1
            # print ('double_exp_podium_counter', double_exp_podium_counter)
            f = 1#cbeme
            g = 0#indice
            h = 3#score
            try :
                if current_challenge>1 :
                    challengeprec = current_challenge-2
                    print ('chall', challengeprec)
                    print ("nbQxallgagnantx, top3NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                    print (len(top3NamesQall), top3NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
                
                if double_exp_podium_counter in (1, 2, 7, 9, 13, 15, 25, 29, 31, 39, 41, 45, 50, 53, 55, 60, 65, 67, 78, 85, 90) and message.author.id not in (brice_identifiant, brice_identifiant):
                    if message.author.name in totdico and current_challenge > 1 :
                        totdico[message.author.name] += 2
                        await message.channel.send('Bravo à ' + message.author.name + ' Phoebe Halliwell : est allé vous cherchez 2 points bonus avec sa magie :)')
                        await message.channel.send(file=discord.File('./assets/charmed2.gif'))
                        if message.author.dm_channel == None : 
                            help_message = 'l\'user ' + message.author.name + ' à gagner 2 pts avec podiumprec, current_challenge:'+ str(current_challenge)
                            await message.author.create_dm()
                            await message.author.send(str(help_message))    
                    elif message.author.name not in totdico and message.author.name not in top3NamesQY : 
                        totdico[message.author.name] = 3
                        await message.channel.send('Bravo à ' + message.author.name + ' Phoebe Halliwell : est allé vous cherchez vos 3 er points bonus avec sa magie')
                        await message.channel.send(file=discord.File('./assets/charmed2.gif'))
                        if message.author.dm_channel == None :
                            help_message = 'l\'user ' + message.author.name + ' à gagner ses 3ers pts avec podiumprec, current_challenge:'+ str(current_challenge)
                            await message.author.create_dm()
                            await message.author.send(str(help_message))  
                while h <= 3 and f <= 3 and g < 3 :
                    print ('g=', g)
                    print ('f=', f)
                    print ('h=', h)
                    await message.channel.send('utilisateur ' + str(top3NamesQall[challengeprec][g]) +  ' Top ' + str(f) + ' a '+str(h) + ' points' )
                    h -= 1
                    f += 1
                    g += 1
                # if double_exp_podium_counter in (1, 2, 7, 9, 13, 15, 25, 29, 31, 39, 41, 45, 50, 53, 55, 60, 65, 67, 78, 85, 90) and message.author.id not in (brice_identifiant, brice_identifiant):
                #     if message.author.name in totdico and current_challenge > 1 :
                #         print(totdico[message.author.name])
                #         totdico[message.author.name] += 2
                #         await message.channel.send('Bravo à ' + message.author.name + ' Phoebe Halliwell : est allé vous cherchez 2 points bonus avec sa magie\
                #             \n c\'est bien de tester :)')
                #         if message.author.dm_channel == None : 
                #             help_message = 'l\'user ' + message.author.name + ' à gagner 2 pts avec podiumprec, current_challenge:'+ str(current_challenge)
                #             await message.author.create_dm()
                #             await message.author.send(str(help_message))    
                #     elif message.author.name not in totdico and message.author.name not in top3NamesQY : 
                #         totdico[message.author.name] = 3
                #         await message.channel.send('Bravo à ' + message.author.name + ' Phoebe Halliwell : est allé vous cherchez vos 3 er points bonus avec sa magie \
                #             \n c\'est bien de tester')
                #         if message.author.dm_channel == None :
                #             help_message = 'l\'user ' + message.author.name + ' à gagner ses 3ers pts avec podiumprec, current_challenge:'+ str(current_challenge)
                #             await message.author.create_dm()
                #             await message.author.send(str(help_message))                  
            except (IndexError) :
                await message.channel.send("Personne d'autres a gagné") #Impossible de trouver l'élément dans la liste
                await message.channel.send(file=discord.File('./assets/done.gif'))
                
                #afficher le podium du challenge terminé que l'on souhaite voir
        if message.content.startswith('!podium') :
            exp_counter_podium += 1
            print('podium', exp_counter_podium)
            podiumnum(message)
            f = 1#cbeme
            g = 0#indice
            h = 3#score
            try:
                if current_challenge > numberpodium :
                    # print ("current_challenge=",current_challenge)
                    # challengeprec=current_challenge-2
                    # challengeprec=int(numberpodium)+1
                    challengeprec = numberpodium-1
                    print ('chall', challengeprec)
                    print ("nbQxallgagnantx, top3NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                    print (len(top3NamesQall), top3NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
                elif current_challenge == numberpodium :
                    await message.channel.send("Ce challenge est en cours !! Veuillez attendre qu'il soit terminé !")
                else: 
                    await message.channel.send("Ce challenge n'a pas démarré!!")
                if exp_counter_podium in (3, 5, 10, 15, 20, 27, 30, 39, 45, 47, 50, 51, 55, 60, 65, 67, 78, 85, 90) and message.author.id not in (brice_identifiant, brice_identifiant) :
                    if message.author.name in totdico and current_challenge > 1 :
                        print(totdico[message.author.name])
                        totdico[message.author.name] += 2
                        print("i'm368")
                        await message.channel.send('Bravo à ' + message.author.name + ' Clara OSWALD : est allé vous cherchez 2 points bonus dans le Tardis')
                        await message.channel.send(file=discord.File('./assets/tardis.gif'))
                        # user=str(476338851871326219)
                        # exp_podium_message='l\'user ' + message.author.name + '2 points grâce à !Podium \n gagné grâce à ' + exp_counter_podium + 'fois'
                        # await client.send_message(user, str(exp_podium_message))
                        # user_brice=str(brice_identifiant)
                        # await client.send_message(user_brice, str(exp_podium_message))
                    elif message.author.name not in totdico and message.author.name not in top3NamesQY :
                        totdico[message.author.name] = 2
                        await message.channel.send('Bravo à ' + message.author.name + ' Clara OSWALD : est allé vous cherchez vos 2 er points bonus dans le Tardis')
                        await message.channel.send(file=discord.File('./assets/tardis.gif'))
                        # user=str(476338851871326219)
                        # exp_podium_message='l\'user ' + message.author.name + 'ses 2 er points grâce à !Podium \n gagné grâce à ' + str(exp_counter_podium) + 'fois'
                        # await client.send_message(user, str(exp_podium_message))
                        # user_brice=str(brice_identifiant)
                        # await client.send_message(user_brice, str(exp_podium_message))
                while h <= 3 and f <= 3 and g < 3 :
                    print ('g=', g)
                    print ('f=', f)
                    print ('h=', h)
                    await message.channel.send('utilisateur ' + str(top3NamesQall[challengeprec][g]) +  ' Top ' + str(f) + ' a '+str(h) + ' points' )
                    h -= 1
                    f += 1
                    g += 1
            except (IndexError) :
                await message.channel.send("Personne d'autres a gagné")#Impossible de trouver l'élément dans la liste
                await message.channel.send(file=discord.File('./assets/done.gif'))

    # Pour les personnes qui peuvent lancer le Challenge
        if message.content.casefold() == 'Challenge!!'.casefold() \
             and message.author.id in (myAuthorId, brice_identifiant, 480045172630224916, clara_oswald) :
            # and prof_grp_id in [y.id for y in Member(message.author).roles] or dev_grp_id in [y.id for y in Member(message.author).roles] :
            # and message.author.id in (myAuthorId, brice_identifiant, 480045172630224916) or prof_grp_id in [y.id for y in message.author.roles] or dev_grp_id in [y.id for y in message.author.roles] :
             # and message.author.id in (myAuthorId, brice_identifiant, 480045172630224916) :
            if (current_challenge >= 1) :
                fini_challenge(top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY)

            if current_challenge == 0 :
                init_list()
            fichreaderq1()
            
            if current_challenge == len(listchallengeq) :
                fini_challenge(top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY)
                podiumsave(message.author.name)
                await message.channel.send('Gagnant tot= ' + str(totdico))
                await message.channel.send("Tous les challenges sont désormais terminés")
                current_challenge += 1

            await message.channel.send(listchallengeq[current_challenge])
            if current_challenge > 0 :
                try :
                    podiumsave(message.author.name)
                    await message.channel.send('Gagnant tot= ' + str(totdico))
                    print ('totdico', totdico)
                    print ("top3NamesQY!!", top3NamesQY)
                except (IndexError) :
                    print ("fini")#Impossible de trouver l'élément dans la liste
            current_challenge += 1
            init_list()

       
       
        if message.content.casefold() == 'help!!'.casefold() :
            help_counter += 1
            await message.channel.send('```!!podium affiche le podium précédent à partir du Challenge 2 pour tous les utilisateurs```'+\
                '```!podium x affiche le podium en fonction du numéro x précédent pour tous les utilisateurs```'\
                + "```PodiumGlobal!! affiche le podium Global des challenges terminés destinés pour tous les utilisateurs```" +\
                '```!podium 0 Affiche le podium du dernier challenge terminé pour tous les utilisateurs```' + '```Challenge!! lancer le challenge ou passer le challenge admin/prof```'\
                + '```Podium!!! voir le podium du challenge actuel pour les admin/prof```')
            if help_counter in (1, 2, 7, 9, 17, 19, 20, 27, 33, 39, 45, 47, 50, 53, 55, 60, 65, 67, 78, 85, 90) and message.author.id not in (brice_identifiant, brice_identifiant) :
                        if message.author.name in totdico and current_challenge > 1 :
                            print(totdico[message.author.name])
                            totdico[message.author.name] += 2
                            print("i'm368")
                            await message.channel.send('Bravo à ' + message.author.name + ' Kara Danvers : est allé vous cherchez 2 points bonus en volant\
                                \n c\'est bien de lire l\'aide :)')
                            await message.channel.send(file=discord.File('./assets/kara.gif'))
                            if message.author.dm_channel == None : 
                            # if client.get_member(myAuthorId) == True :
                                print('im500')
                                help_message = 'l\'user ' + message.author.name + ' à gagner 2 pts avec help, current_challenge:'+ str(current_challenge)
                                await message.author.create_dm()
                                await message.author.send(str(help_message))    
                        # elif message.author.name in top3NamesQY and current_challenge == 1 :
                        #     # print(top3NamesQY[message.author.name])
                        #     # print(top3NamesQY)
                        #     print(totdico)
                        #     totdico[message.author.name] += 2
                        #     print("i'm368!")
                        #     await message.channel.send('Bravo à ' + message.author.name + ' Kara Danvers : est allé vous cherchez 2 points bonus en volant\
                        #         \n c\' est bien de lire l\'aide :)')
                        #     if message.author.dm_channel == None : 
                        #         print('im500!')
                        #         help_message = 'l\'user ' + message.author.name + ' à gagner 2 pts avec help, current_challenge:'+ str(current_challenge)
                        #         await message.author.create_dm()
                        #         await message.author.send(str(help_message))    
                        elif message.author.name not in totdico and message.author.name not in top3NamesQY : 
                            totdico[message.author.name] = 3
                            await message.channel.send('Bravo à ' + message.author.name + ' Kara Danvers : est allé vous cherchez vos 3 er points bonus en volant \
                                \n c\'est bien il faut toujours lire la consigne avant de commencer')
                            await message.channel.send(file=discord.File('./assets/kara.gif'))
                            if message.author.dm_channel == None :
                            # if client.get_member(myAuthorId) == True :
                                print('im500')
                                help_message = 'l\'user ' + message.author.name + ' à gagner ses 3ers pts avec help, current_challenge:'+ str(current_challenge)
                                await message.author.create_dm()
                                await message.author.send(str(help_message))   

        # if reaction.emoji == '👍' :
        #     if message.author.name in totdico and current_challenge > 1 :
        #         print(totdico[message.author.name])
        #         totdico[message.author.name] += 2
        #         await message.channel.send('Bravo à ' + message.author.name + ' Clara OSWALD : est allé vous cherchez 2 points bonus dans le Tardis')
        #         await message.channel.send(file=discord.File('./assets/tardise.gif'))

        #     elif message.author.name not in totdico and message.author.name not in top3NamesQY :
        #         totdico[message.author.name] = 2
        #         await message.channel.send('Bravo à ' + message.author.name + ' Clara OSWALD : est allé vous cherchez vos 2 er points bonus dans le Tardis')
        #         await message.channel.send(file=discord.File('./assets/tardise.gif'))
        # elif reaction.emoji == '👎':
        #     if message.author.name in totdico and current_challenge > 1 :
        #         totdico[message.author.name] -= 2
        #         await message.channel.send('Pour ' + message.author.name + ' Clara OSWALD : est allé vous retirez 2 points avec le Tardis')
        #         await message.channel.send(file=discord.File('./assets/tardise.gif'))

            elif message.author.name not in totdico and message.author.name not in top3NamesQY :
                totdico[message.author.name] = -2
                await message.channel.send('Pour ' + message.author.name + ' Clara OSWALD : est allé vous retirez vos 2 er points avec le Tardis')
                await message.channel.send(file=discord.File('./assets/tardise.gif'))
        # print ('cr',current_challenge)
        # if message.content == listchallenger[current_challenge-1] and message.channel.id == my_channel_id3 and current_challenge < len(listchallengeq) :
        if message.content == listchallenger[current_challenge-1] and message.channel.id == my_channel_id3 :
        # if message.content == listchallenger[current_challenge-1] or message.content == 'la bonne réponse est ' + listchallenger[current_challenge - 1] and message.channel.id == my_channel_id3 :
        # if message.content.casefold() == listchallenger[current_challenge].casefold() :
        # print ('listcr', listchallenger[current_challenge-1])
            print (message.content)
            await message.delete()#discord.errors.Forbidden: 403 Forbidden (error code: 50013): Missing Permissions
            await message.channel.send(message.author.name + " Vous devez saisir la réponse en message privée!!! \n -2Points ROHH!! ```Attention Bart tu vas avoir une punition ...```")
            await message.channel.send(file=discord.File('./assets/bartpu.gif'))
            #boucle while Clodomir permet de retirer aux utilisateurs dans totdico les malus des gens qui répondent dans le channel
            # if message.author.name in totdico :
            #     totdico[message.author.name] -= 2
            # else : 
            #     totdico[message.author.name] = -2
            fact_malus (totdico, message.author.name)   #Boucle clodomir V2

            # await client.delete_message(message)# AttributeError: 'Bot' object has no attribute 'delete_message' AttributeError: 'Bot' object has no attribute 'delete_messages'
        # elif message.content == listchallenger[current_challenge-1] and message.channel.id == my_channel_id3 and challengefinaled == 0 :
        #     print ('Tous les Challenges sont terminés !!!')
       
        # Dans le channel privée et si ce n'est pas le bot
        if isinstance(message.channel, discord.DMChannel) and message.author.id != BOTman_id :
            print ("Message privé : " + message.author.name + ":" + message.content)
            fichreaderq1()
            listchallengerx = listchallenger[current_challenge-1]
            print ("nbQxgagnant, top3NamesQY, ontBonMaisTropTardQY,  perduAnImporteQuelQY")
            print (len(top3NamesQY), top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY)
            if current_challenge > 1 :
                print ("nbQxallgagnant, top3NamesQall, ontBonMaisTropTardQall,  perduAnImporteQuelQall")
                print (len(top3NamesQall), top3NamesQall, ontBonMaisTropTardQall, perduAnImporteQuelQall)
                challengeprec = current_challenge-2
                print ('chall', challengeprec)
                print ("nbQxallgagnantx, top3NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                print (len(top3NamesQall), top3NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
            # print ('message utilisateur=', message.content)
            # print ('réponse=', listchallengerx)

            if reptricheur(top3NamesQY, listchallengerx, message) != True :
                await message.channel.send(reptriche1) 
            
            if repondre_quest(message, listchallengerx, top3NamesQY, ontBonMaisTropTardQY,'Q' + str(current_challenge)) == True :
                # await message.channel.send(msggagne+str(current_challenge))      
                await message.channel.send(msggagne + str(current_challenge) + "\n" + homer)  
                await message.channel.send(file=discord.File('./assets/homer.gif'))
                print('im519')    
                if message.author.dm_channel == True : 
                # if client.get_member(myAuthorId) == True :
                    print('im520')
                    exp_podium_message='l\'user ' + message.author.name + 'à gagner au challenge'+ str(current_challenge)
                    await message.author.create_dm()
                    await message.author.send(str(exp_podium_message))     

                
                # await message.channel.send(homer) 
    
                    # await client.send_message(user, )
                    # user_brice=str(brice_identifiant)
                    # await client.send_message(myAuthorId, str(exp_podium_message))

            if len(top3NamesQY) > 3 :
                await message.channel.send(repbotlate1)
                await message.channel.send(repbotlate1bis)
                ontBonMaisTropTardQY.append(message.author.name) #sinon bug si refacto
            
            if message.content.casefold() == listchallengerx.casefold() and reptricheur(top3NamesQY, listchallengerx, message) != True :
            #     await message.channel.send(homer)      
                  truc = None#cette fonction sert à n'envoyer que si c'est la mauvaise réponseet ou l'utilisateur reparticipe évite le else
            elif message.author.name in top3NamesQY : # cette fonction permet de ne pas afficher de message au tricheur
                arretedeparticiper = None#arretedeparticiper bordel permet d'utiliser cette fonction
            else :
                await message.channel.send('Mauvaise réponse') 
                perduAnImporteQuelQY.append(message.author.name)
                await message.channel.send(file=discord.File('./assets/perdu.gif'))


            print ("nbQxgagnant, top3NamesQY, ontBonMaisTropTardQY,  perduAnImporteQuelQY", "totdico")
            print (len(top3NamesQY), top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY, totdico)

        # Dans le channel général et si c'est moi/Augustin bientôt        
        # elif message.author.name == myAuthorId:
        elif message.author.name == 'AMINE AA' :
            print ("Mon message dans le channel général :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS UP SIGN}')
        elif message.author.id == brice_identifiant :
            print ("Message de Brice dans le channel général :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS UP SIGN}')  
        #Si ce n'est pas le bot
        elif not isinstance(message.channel, discord.DMChannel) and message.author.id == BOTman_id :
            print ("Message du BOT dans le channel général :", message.content)
            # await message.add_reaction(emoji = '\N{THUMBS UP SIGN}')

        # Dans le channel et si c'est n'importe qui autre que moi
        elif not isinstance(message.channel, discord.DMChannel) :
            print ("Message par qq d'autres du channel :", message.content)
            # await message.add_reaction(emoji = '\N{THUMBS DOWN SIGN}')
        # Message du Bot     
        elif message.author.id == BOTman_id :
            print ("Message du bot :", message.content)
            # await message.add_reaction(emoji = '\N{THUMBS UP SIGN}') 
        #si channel n'est le channel du prof/le mien par Augustin
        elif message.channel.id != my_channel_id :
            return
        # Tous les autres cas
        else :
            print ("Tous les autres cas :", message.content)
            # await message.add_reaction(emoji = '\N{THUMBS DOWN SIGN}')
    except (RuntimeError) :
        print ("Une erreur est survenue...Fermeture")
        sys.exit(1)        

# @client.event
# async def on_reaction_add(reaction, user):
    

client.run(token[0])
