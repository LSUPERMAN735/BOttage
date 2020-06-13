#!/usr/bin/env python3
# -- coding: utf-8 --
#4may , 5 may , 6 may commencé vers 18H20 , 7 may , 11 may , 12 may , 13 may, and 14 may, 15 may and 18 may,19may,21may, 25 may,27, 29 may,5juin,6juin,7juin, 8juin, 9juin, 10juin
#11juin, 12juin et rapport 13juin
#sort added for podiumglobal and added !podium x, podiumsave dans challenge!!
#lisibility added, gif, time easteregg
#crédits Amine ABDOUL-AZID, Brice AUGUSTIN, UPEC
#licence GNU V3 à copier avec les termes
#    GNU GENERAL PUBLIC LICENSE
#    Version 3, 29 June 2007
import sys
import discord
from discord.ext import commands
from operator import itemgetter
import asyncio
from datetime import datetime
import random

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
role_roi_id = 719298857191604274


top3NamesQall = []
ontBonMaisTropTardQall = []
perduAnImporteQuelQall = []
#variable
current_challenge = 0
#easteregg counter
exp_counter_podium = 0
help_counter = 0
podium_global_counter = 0
double_exp_podium_counter = 0
credits_counter = 0
show_counter = 0

perdu_counter = 0
thisisuniq = 0 # commentable normalement

block_it = []
isuniq_list = [] #car buggue sinon
#liste to block to one easteregg for people by categories
credits_gagnant = []
exp_gagnant_podium = []
help_gagnant = []
podium_global_gagnant = []
double_exp_podium_gagnant = []
show_gagnant = []
####
# Events
####
client = commands.Bot(command_prefix='.')

# #challenge rép -> fichier fichreaderq1() fini les brut
#réponse rapide réponse type du bot
#réponse du bot en cas de victoire
msggagne = 'Vous avez bon à la question '
#réponse bot en cas de de victoire
homer = 'Homer: Woohoo!! Vous êtes trop fort!!'
# rep triche:
reptriche1 = 'Vous avez déjà participé ! Faîtes autre chose !!'
reptriche2 = 'tente de tricher!!'

#reponse si trop tard du bot
repbotlate1 = 'Mais 3 autres personnes ont déjà gagné, vous êtes trop lent donc 0 point '
repbotlate1bis = 'Soyez plus rapide à la prochaine question '


totdico = {}
#définition des fonctions

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
    else: #commentable
        return True #commentable

        #casefold pour ignorer la casse majuscule, minuscule ou mélangées
def repondre_quest(msg, repx, top3NamesQx, ontBonMaisTropTardQx, Qx):
    if msg.content.casefold() == repx.casefold() and reptricheur(top3NamesQx, repx, msg) == True :
        print (msggagne,Qx)
        print (msg.author.name)
        top3NamesQx.append(msg.author.name)
        print ('gagné', Qx, '=', len(top3NamesQx)) #debug
        print ('gagné', Qx, 'mais late =', len(ontBonMaisTropTardQx)) #debug
        return True

def fichreaderq1() :
    global quest, rep, listchallengeq, listchallenger, rep2, isuniq
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
        isuniq = delims[2]
        isuniq_list.append(isuniq)

    fichdeqr.close()
    return quest, rep

def podiumsave(message_author_name) : #time comp added
    global totdico, top3NamesQY
    global debut_time, debut_final, zetime, heure_bool
    zetime = datetime.now()
    debut_time = 00 #22 utc
    final_time = 5 #3 utc
    heure_bool = 0
    if debut_time <= zetime.hour <= final_time :
        print ('heure! :', zetime.hour)
        heure_bool += 1
    else :#commentable
        print ('elseheure! :', zetime.hour)#commentable

    i = 3#score
    print ('top3NameQY=', top3NamesQY)
    for s in top3NamesQY :
        print ('current_challenge!', current_challenge)
        if i > 0 : #permet de ne prendre que le top x avec point positif et permet d'éviter un score négatif sauf si affecté en malus pour tous les gens en retard ou perdant
            if current_challenge >= 1 and heure_bool == 0 : 
                try: 
                    totdico[s] += i
                    i -= 1
                except KeyError :
                    totdico[s] = i
                    i -= 1
                    print ('exception')#debug

            elif current_challenge >= 1 and heure_bool == 1 : 
                try: 
                    totdico[s] += i * 2
                    i -= 1
                except KeyError :
                    totdico[s] = i * 2
                    i -= 1
                    print ('exception')#debug
            else :#commentable
                print ('fini')#commentable
    return totdico

def podiumnum(message) :
    global typed, delimited, podiuming, numberpodiuming, numberpodium
    typed = message.content
    delimited = typed.split(' ') 
    podiuming = delimited[0]
    numberpodiuming = delimited[1]
    numberpodium = int(numberpodiuming)
    print ("message= " + message.content)#debug
    print ("podiuming= " + podiuming)#debug
    print ("numberpodium= " + numberpodiuming) #debug
    return typed, delimited, podiuming, numberpodiuming, numberpodium

def fact_malus(totdico, message_author_name) : # sert à retirer les points malus si réponse dans le salon sauf si challenge 1
            if message_author_name in totdico :
                totdico[message_author_name] -= 2
            else : 
                totdico[message_author_name] = -2
   
@client.event
async def on_ready() :
    print ('Challenge Bot est prêt.')
    return True        

@client.event
async def on_message(message) :
    try:
        # global appel_membre, appel, absents, presents
        global perdu_counter, block_it,  show_counter, credits_counter , isuniq, thisisuniq
        global credits_gagnant, exp_gagnant_podium, help_gagnant, podium_global_gagnant, double_exp_podium_gagnant, show_gagnant
        global exp_counter_podium, help_counter, double_exp_podium_counter, podium_global_counter, debut_time, final_time, zetime, heure_bool
        # global o
        global top3NamesQall, ontBonMaisTropTardQall, perduAnImporteQuelQall, poder
        global current_challenge, totdico, top3NamesQY
        zeid = message.author.id
        zename = message.author.name
        if thisisuniq == 0 :
            block_it = []
            thisuniq = 0
        if message.author.id != BOTman_id :
            print ("Je suis", zename)
            print ("Actuellement les valeurs sont :")
            print ("my_channel_id, BOTman_id, myAuthorId", \
                my_channel_id, BOTman_id, myAuthorId)
            
            print ("Message initial", message)

        if message.content.casefold() == 'Podium!!!'.casefold() \
            and message.author.id in (myAuthorId, brice_identifiant, 480045172630224916) and role_roi_id in [y.id for y in message.author.roles] : #current_podiums only for admins/dev/teachers
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

        
        if message.content.casefold() == 'PodiumGlobal!!'.casefold() and role_roi_id in [y.id for y in message.author.roles] : #podium global par les admins
            podium_global_counter += 1
            if current_challenge == 1 :
            # print ('podium_global_counter', podium_global_counter)
            # r.id in (myAuthorId, brice_identifiant, 480045172630224916) or prof_grp_id in [y.id for y in message.author.roles] or dev_grp_id in [y.id for y in message.author.roles] : 
                await message.channel.send("Veuillez attendre que le challenge soit terminé ou faites Podium!!! si vous êtes prof")
      
            try :
                o = 1#init variable global podium
                s = ''
                formatage = ''
                for cle, valeur in sorted(totdico.items(), key = itemgetter(1), reverse = True): #itemgetter 1 car on trie par rapport au score, reverse true trier a>b
                    if valeur > 0 and current_challenge > 1 : #ne met ni d'erreur mais n'affiche pas que les valeurs supérieurs à 0 pour bloquer l'affichage 
                        s = s + str(cle) + ' Top ' + str(o) + ' a ' + str(valeur) + ' points' + '\n'
                        o += 1
                if s == '' : 
                    await message.channel.send("Personne d'autres a gagné") 
                    await message.channel.send(file=discord.File('./assets/done.gif')) 
                else : 
                    await message.channel.send(s)
                #Impossible de trouver l'élément dans la liste
                
                if podium_global_counter in (1, 2, 7, 9, 14, 15, 21, 23, 31, 39, 41, 45, 50, 53, 55, 60, 65, 67, 78, 85) and message.author.id not in (brice_identifiant, brice_identifiant) :
                            if zename in totdico and zename not in podium_global_gagnant :
                                totdico[zename] += 2
                                podium_global_gagnant.append(zename)
                                await client.get_user(zeid).send('Bravo à ' + zename + ' BENDER : est allé vous cherchez 2 points bonus dans le FUTURama\
                                    \n c\'est bien de checker :)')
                                await client.get_user(zeid).send(file=discord.File('./assets/bender.gif'))
                                podium_global_message = zename + ' a gagné 2 pts avec podiumglob, current_challenge: '+ str(current_challenge) + ' car '\
                                    + str(podium_global_counter) + ' fois'
                                await client.get_user(myAuthorId).send(podium_global_message)
                                await client.get_user(brice_identifiant).send(podium_global_message)
                            elif zename not in totdico and zename not in top3NamesQY and zename not in podium_global_gagnant : 
                                totdico[zename] = 2
                                podium_global_gagnant.append(zename)
                                await client.get_user(zeid).send('Bravo à ' + zename\
                                     + ' BENDER : est allé vous cherchez vos 2 er points bonus dans le FUTURama\
                                    \n c\'est bien de checker')
                                await client.get_user(zename).send(file=discord.File('./assets/bender.gif'))
                                podium_global_message = zename + ' a gagné ses 3ers pts avec podiumglob, current_challenge: '+ str(current_challenge) + ' car '\
                                    + str(podium_global_counter) + ' fois'
                                await client.get_user(myAuthorId).send(podium_global_message)
                                await client.get_user(brice_identifiant).send(podium_global_message)
                            elif zename in totdico and current_challenge > 1 and zename in podium_global_gagnant :
                                await client.get_user(zeid).send('Désolé mais je ne peux vous attribuer des points bonus avec cette commande laissez-les pour les autres')
                                podium_global_counter -= 1
            except (IndexError) :
                await message.channel.send("Personne d'autres a gagné")#Impossible de trouver l'élément dans la liste
                await message.channel.send(file=discord.File('./assets/done.gif'))


        if message.content.casefold() == '!!podium'.casefold() and role_roi_id in [y.id for y in message.author.roles] :
            double_exp_podium_counter += 1
            # print ('double_exp_podium_counter', double_exp_podium_counter)
            f = 1#cbeme
            g = 0#indice
            h = 3#score
            try :
                if current_challenge > 1 :
                    challengeprec = current_challenge-2
                    print ('chall', challengeprec)
                    print ("nbQxallgagnantx, top3NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                    print (len(top3NamesQall), top3NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
                if current_challenge <= 1 :
                    await message.channel.send('C\'est bien de tester les commandes mais cette commande s\'utilisent à partir du Challenge 2' )
                #boucle Flash
                if double_exp_podium_counter in (1, 2, 7, 9, 13, 15, 25, 29, 31, 39, 41, 45, 50, 53, 55, 60, 65, 67, 78, 85, 90) and message.author.id not in (brice_identifiant, brice_identifiant):
                    if zename in totdico and current_challenge > 1 and zename not in double_exp_podium_gagnant :
                        totdico[zename] += 2
                        double_exp_podium_gagnant.append(zename)
                        await client.get_user(zeid).send('Bravo à ' + zename + ' Phoebe Halliwell : est allé vous cherchez 2 points bonus avec sa magie :)')
                        await client.get_user(zeid).send(file=discord.File('./assets/charmed2.gif'))
                        double_exp_podium_message = zename + ' a gagné 2 pts avec podiumprec, current_challenge: '+ str(current_challenge) + ' car '\
                             + str(double_exp_podium_counter) + ' fois'
                        await client.get_user(myAuthorId).send(double_exp_podium_message)
                        await client.get_user(brice_identifiant).send(double_exp_podium_message)
                         
                    elif zename not in totdico and zename not in top3NamesQY and zename not in double_exp_podium_gagnant : 
                        totdico[zename] = 3
                        double_exp_podium_gagnant.append(zename)
                        await client.get_user(zeid).send('Bravo à ' + zename + \
                            ' Phoebe Halliwell : est allé vous cherchez vos 3 er points bonus avec sa magie')
                        await client.get_user(zeid).send(file=discord.File('./assets/charmed2.gif'))
                        double_exp_podium_message = zename + ' a gagné ses 3ers pts avec podiumprec, current_challenge: '+ str(current_challenge) + ' car '\
                             + str(double_exp_podium_counter) + ' fois'
                        await client.get_user(myAuthorId).send(double_exp_podium_message)
                        await client.get_user(brice_identifiant).send(double_exp_podium_message)
                    elif zename in totdico and current_challenge > 1 and zename in double_exp_podium_gagnant :
                            await client.get_user(zeid).send('Désolé mais je ne peux vous attribuer des points bonus avec cette commande laissez-les pour les autres')
                            double_exp_podium_counter -= 1
                while h <= 3 and f <= 3 and g < 3 :
                    await message.channel.send('utilisateur ' + str(top3NamesQall[challengeprec][g]) +  ' Top ' + str(f) + ' a '+str(h) + ' points' )
                    h -= 1
                    f += 1
                    g += 1
                    #si ici ça buggue  pour la boucle Flash      
            except (IndexError) :
                await message.channel.send("Personne d'autres a gagné") #Impossible de trouver l'élément dans la liste
                await message.channel.send(file=discord.File('./assets/done.gif'))
                
                #afficher le podium du challenge terminé que l'on souhaite voir
        if message.content.startswith('!podium') and role_roi_id in [y.id for y in message.author.roles] :
            exp_counter_podium += 1
            print ('podium', exp_counter_podium)
            podiumnum(message)
            f = 1#cbeme
            g = 0#indice
            h = 3#score
            try:
                if current_challenge > numberpodium :
                    challengeprec = numberpodium-1
                    print ('chall', challengeprec)
                    print ("nbQxallgagnantx, top3NamesQallx, ontBonMaisTropTardQallx,  perduAnImporteQuelQallx")
                    print (len(top3NamesQall), top3NamesQall[challengeprec], ontBonMaisTropTardQall[challengeprec], perduAnImporteQuelQall[challengeprec])
                elif current_challenge == numberpodium :
                    await message.channel.send("Ce challenge est en cours !! Veuillez attendre qu'il soit terminé !")
                else: 
                    await message.channel.send("Ce challenge n'a pas démarré!!")
                if exp_counter_podium in (3, 5, 10, 15, 20, 27, 30, 39, 45, 47, 50, 51, 55, 60, 65, 67, 78, 85, 90) and message.author.id not in (brice_identifiant, brice_identifiant) :
                    
                    if zename in totdico and current_challenge > 1 :
                        # print(totdico[zename])#debug
                        totdico[zename] += 2
                        exp_gagnant_podium.append(zename)
                        await client.get_user(zeid).send('Bravo à ' + zename + ' Clara OSWALD : est allé vous cherchez 2 points bonus dans le Tardis')
                        await client.get_user(zeid).send(file=discord.File('./assets/tardis.gif'))
                        exp_podium_message=zename + '2 points grâce à !Podium \n gagné grâce à podiumx car ' + str(exp_counter_podium) + ' fois'
                        await client.get_user(myAuthorId).send(exp_podium_message)
                        await client.get_user(brice_identifiant).send(exp_podium_message)

                    elif zename not in totdico and zename not in top3NamesQY :
                        totdico[zename] = 2
                        exp_gagnant_podium.append(zename)
                        await client.get_user(zeid).send('Bravo à ' + zename + ' Clara OSWALD : est allé vous cherchez vos 2 er points bonus dans le Tardis')
                        await client.get_user(zeid).send(file=discord.File('./assets/tardis.gif'))
                        exp_podium_message=zename + 'ses 2er points grâce à !Podium \n gagné grâce à podiumx car ' + str(exp_counter_podium) + ' fois'
                        await client.get_user(myAuthorId).send(exp_podium_message)
                        await client.get_user(brice_identifiant).send(exp_podium_message)
                    elif zename in totdico and current_challenge > 1 and zename in exp_gagnant_podium :
                            await client.get_user(zeid).send('Désolé mais je ne peux vous attribuer des points bonus avec cette commande laissez-les pour les autres')
                            exp_counter_podium -= 1

                while h <= 3 and f <= 3 and g < 3 :
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
            if (current_challenge >= 1) :
                fini_challenge(top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY)

            if current_challenge == 0 :
                init_list()
            fichreaderq1()
            
            if current_challenge == len(listchallengeq) :
                fini_challenge(top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY)
                podiumsave(zename)
                # await message.channel.send('Gagnant tot= ' + str(totdico))
                await message.channel.send("Tous les challenges sont désormais terminés")
                current_challenge += 1

            await message.channel.send(listchallengeq[current_challenge])
            if current_challenge > 0 :
                try :
                    podiumsave(zename)
                    # await message.channel.send('Gagnant tot= ' + str(totdico))
                    print ('totdico', totdico) #debug
                    print ("top3NamesQY!!", top3NamesQY) #debug
                    block_it = []
                    # del block_it[:] #forcer le reset 
                except (IndexError) :
                    print ("fini")#Impossible de trouver l'élément dans la liste
            if isuniq_list[current_challenge] == 'uniq' : #bloque à une participation et envoie le message sur le salon
                await message.channel.send('Ce test est bloqué à une participation')
                thisisuniq = 1
            else :
                thisisuniq = 0 # si ce n'est pas un challenge OUI ou NON
            current_challenge += 1
            init_list()

       
       
        if message.content.casefold() == 'help!!'.casefold() and role_roi_id in [y.id for y in message.author.roles] :
            help_counter += 1
            await message.channel.send('```!!podium affiche le podium précédent à partir du Challenge 2 pour tous les utilisateurs```'+\
                '```!podium x affiche le podium en fonction du numéro x précédent pour tous les utilisateurs```'\
                + "```PodiumGlobal!! affiche le podium Global des challenges terminés destinés pour tous les utilisateurs```" +\
                '```!podium 0 Affiche le podium du dernier challenge terminé pour tous les utilisateurs```' +\
                 '```Show : Affiche les consignes du challenge en cours pour tous les utilisateurs ```'+\
                    '```Credits!! : Affiche les crédits concepteur pour tous les utilisateurs```'+\
                    '```Challenge!! lancer le challenge ou passer le challenge admin/prof```'\
                + '```Podium!!! voir le podium du challenge actuel pour les admin/prof```')
            if help_counter in (1, 2, 7, 9, 17, 19, 20, 27, 33, 39, 45, 47, 50, 53, 55, 60, 65, 67, 78, 85, 90) and message.author.id not in (brice_identifiant, brice_identifiant) :
                        if zename in totdico and current_challenge > 1  and zename not in help_gagnant :
                            totdico[zename] += 2
                            help_gagnant.append(zename)
                            await client.get_user(zeid).send('Bravo à ' + zename + ' Kara Danvers : est allé vous cherchez 2 points bonus en volant\
                                \n c\'est bien de lire l\'aide :)')
                            await client.get_user(zeid).send(file=discord.File('./assets/kara.gif'))
                            help_message = zename + ' a gagné 2 pts avec help, au challenge: ' + str(current_challenge) + ' car ' + str(help_counter) + ' fois'
                            await client.get_user(myAuthorId).send(help_message)
                            await client.get_user(brice_identifiant).send(help_message)
                        elif zename not in totdico and zename not in top3NamesQY and zename not in help_gagnant : 
                            totdico[zename] = 3
                            help_gagnant.append(zename)
                            await client.get_user(zeid).send('Bravo à ' + zename + ' Kara Danvers : est allé vous cherchez vos 3 er points bonus en volant\
                                \n c\'est bien de lire l\'aide :)')
                            await client.get_user(zeid).send(file=discord.File('./assets/kara.gif'))
                            help_message = zename + ' a gagné ses 3ers pts avec help, au challenge: ' + str(current_challenge) + ' car '+ str(help_counter) + ' fois'
                            await client.get_user(myAuthorId).send(help_message)
                            await client.get_user(brice_identifiant).send(help_message)
                        elif zename in totdico and current_challenge > 1 and zename in help_gagnant :
                            await client.get_user(zeid).send('Désolé mais je ne peux vous attribuer des points bonus avec cette commande laissez-les pour les autres')
                            help_counter -= 1
        
        if message.content.casefold() == 'credits!!'.casefold() and role_roi_id in [y.id for y in message.author.roles] :
            await message.channel.send('Créé par Amine AA/ABDOUL-AZID, Brice Augustin, amine.abdoul-azid@etu.u-pec.fr/brice.augustin@u-pec.fr UPEC Copyleft https://github.com/LSUPERMAN735 \
                Licence MIT')
            credits_counter += 1
            if credits_counter in (1, 2, 7, 9, 17, 19, 20, 27, 33, 39, 45, 47, 50, 53, 55, 60, 65, 67, 78, 85, 90) and message.author.id not in (brice_identifiant, brice_identifiant) :
                if zename in totdico and current_challenge > 1 and zename not in credits_gagnant :
                    totdico[zename] += 2
                    credits_gagnant.append(zename)
                    await client.get_user(zeid).send('Bravo à ' + zename + ' Alan : vous fait mangé 2 points bonus \
                        \n c\'est bien de se renseigner sur les créateurs :)')
                    await client.get_user(zeid).send(file=discord.File('./assets/alan.gif'))
                    credits_message = zename + ' a gagné 2 pts avec credits, au challenge: ' + str(current_challenge) + ' car ' + str(credits_counter) + ' fois'
                    await client.get_user(myAuthorId).send(credits_message)
                    await client.get_user(brice_identifiant).send(credits_message)
                elif zename not in totdico and zename not in top3NamesQY and zename not in credits_gagnant : 
                    totdico[zename] = 3
                    credits_gagnant.append(zename)
                    await client.get_user(zeid).send('Bravo à ' + zename + ' Alan : vous fait mangé 3 er points bonus \
                        \n c\'est bien de se renseigner sur les créateurs :)')
                    await client.get_user(zeid).send(file=discord.File('./assets/alan.gif'))
                    credits_message = zename + ' a gagné ses 3ers pts avec credits, au challenge: ' + str(current_challenge) + ' car '+ str(credits_counter) + ' fois'
                    await client.get_user(myAuthorId).send(credits_message)
                    await client.get_user(brice_identifiant).send(credits_message)
                elif zename in totdico and current_challenge > 1 and zename in credits_gagnant :
                    await client.get_user(zeid).send('Désolé mais je ne peux vous attribuer des points bonus avec cette commande laissez-les pour les autres')
                    credits_counter -= 1

        if message.content.casefold() == 'show!!'.casefold() and role_roi_id in [y.id for y in message.author.roles] :
            await message.channel.send(listchallengeq[current_challenge-1])
            show_counter += 1
            if show_counter in (1, 2, 7, 9, 17, 19, 20, 27, 33, 39, 45, 47, 50, 53, 55, 60, 65, 67, 78, 85, 90) and message.author.id not in (brice_identifiant, brice_identifiant) :
                if zename in totdico and current_challenge > 1 and zename not in show_gagnant :
                    totdico[zename] += 2
                    show_gagnant.append(zename)
                    await client.get_user(zeid).send('Bravo à ' + zename + ' Natsu : vous fait goûté vos 2 points bonus :)')
                    await client.get_user(zeid).send(file=discord.File('./assets/natsu.gif'))
                    show_message = zename + ' a gagné 2 pts avec show, au challenge: ' + str(current_challenge) + ' car ' + str(show_counter) + ' fois'
                    await client.get_user(myAuthorId).send(show_message)
                    await client.get_user(brice_identifiant).send(show_message)
                elif zename not in totdico and zename not in top3NamesQY and zename not in credits_gagnant : 
                    totdico[zename] = 3
                    show_gagnant.append(zename)
                    await client.get_user(zeid).send('Bravo à ' + zename + ' Natsu : vous fait goûté vos 3 er points bonus :)')
                    await client.get_user(zeid).send(file=discord.File('./assets/natsu.gif'))
                    show_message = zename + ' a gagné ses 3ers pts avec show, au challenge: ' + str(current_challenge) + ' car '+ str(show_counter) + ' fois'
                    await client.get_user(myAuthorId).send(show_message)
                    await client.get_user(brice_identifiant).send(show_message)
                elif zename in totdico and current_challenge > 1 and zename in show_gagnant :
                    await client.get_user(zeid).send('Désolé mais je ne peux vous attribuer des points bonus avec cette commande laissez-les pour les autres')
                    show_counter -= 1
        # else : #supprimable
        #     await message.channel.send('Aucun Challenge a été lancé ou tout les challenges sont terminés!!')#supprimable

        # if reaction.emoji == '👍' :
        #     if zename in totdico and current_challenge > 1 :
        #         print(totdico[zename])
        #         totdico[zename] += 2
        #         await message.channel.send('Bravo à ' + zename + ' Clara OSWALD : est allé vous cherchez 2 points bonus dans le Tardis')
        #         await message.channel.send(file=discord.File('./assets/tardise.gif'))

        #     elif zename not in totdico and zename not in top3NamesQY :
        #         totdico[zename] = 2
        #         await message.channel.send('Bravo à ' + zename + ' Clara OSWALD : est allé vous cherchez vos 2 er points bonus dans le Tardis')
        #         await message.channel.send(file=discord.File('./assets/tardise.gif'))
        # elif reaction.emoji == '👎':
        #     if zename in totdico and current_challenge > 1 :
        #         totdico[zename] -= 2
        #         await message.channel.send('Pour ' + zename + ' Clara OSWALD : est allé vous retirez 2 points avec le Tardis')
        #         await message.channel.send(file=discord.File('./assets/tardise.gif'))

            # elif zename not in totdico and zename not in top3NamesQY :
            #     totdico[zename] = -2
            #     await message.channel.send('Pour ' + zename + ' Clara OSWALD : est allé vous retirez vos 2 er points avec le Tardis')
            #     await message.channel.send(file=discord.File('./assets/tardise.gif'))
        
        
        # print ('cr',current_challenge)#debug
        # if message.content == listchallenger[current_challenge-1] and message.channel.id == my_channel_id3 and current_challenge < len(listchallengeq) :
        if message.content == listchallenger[current_challenge-1] and message.channel.id == my_channel_id3 and role_roi_id in [y.id for y in message.author.roles] :#boucle limitant les réponses dans le salon avec malus
            print (message.content)
            await message.delete()#discord.errors.Forbidden: 403 Forbidden (error code: 50013): Missing Permissions
            await message.channel.send(zename + " Vous devez saisir la réponse en message privée!!! \n -2Points ROHH!! ```Attention Bart tu vas avoir une punition ...```")
            await message.channel.send(file=discord.File('./assets/bartpu.gif'))#sauf bart en publique
            fact_malus (totdico, zename)   #Boucle clodomir V2 permet de retirer aux utilisateurs dans totdico les malus des gens qui répondent dans le channel

            # await client.delete_message(message)# AttributeError: 'Bot' object has no attribute 'delete_message' AttributeError: 'Bot' object has no attribute 'delete_messages'
        # elif message.content == listchallenger[current_challenge-1] and message.channel.id == my_channel_id3 and challengefinaled == 0 :
        #     print ('Tous les Challenges sont terminés !!!')

        # Dans le channel privée et si ce n'est pas le bot
        if isinstance(message.channel, discord.DMChannel) and message.author.id != BOTman_id :
            print ("Message privé : " + zename + ":" + message.content)
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
            # print ('réponse=', listchallengerx)

            if reptricheur(top3NamesQY, listchallengerx, message) != True :
                await message.channel.send(reptriche1) 
                    #si question uniq alors on laisse participer
            if zename not in block_it and thisisuniq == 1 and repondre_quest(message, listchallengerx, top3NamesQY, ontBonMaisTropTardQY,'Q' + str(current_challenge)) == True :
                await message.channel.send('blockit'+str( block_it)) #debug
                await message.channel.send(msggagne + str(current_challenge) + "\n" + homer)  
                await message.channel.send(file=discord.File('./assets/homer.gif'))
                await client.get_user(myAuthorId).send(zename + " a bon au Challenge " + str(current_challenge))
                await client.get_user(brice_identifiant).send(zename + " a bon au Challenge " + str(current_challenge))
                mytime = datetime.now()
                xdebut_time = 00
                xfinal_time = 5
                if xdebut_time <= mytime.hour <= xfinal_time :
                    print ('heure! :', mytime.hour)#debug
                    await message.channel.send('Vos points ont été doublés')
                    await client.get_user(myAuthorId).send(zename + " points doublé au Challenge " + str(current_challenge))
                    await client.get_user(brice_identifiant).send(zename + " points doublé au Challenge " + str(current_challenge))
                else :#commentable
                    print ('elseheure :', mytime)#debug commentable
            elif thisisuniq == 0 and repondre_quest(message, listchallengerx, top3NamesQY, ontBonMaisTropTardQY,'Q' + str(current_challenge)) == True : # si ce n'est pas une question uniqe
                await message.channel.send(msggagne + str(current_challenge) + "\n" + homer)  
                await message.channel.send(file=discord.File('./assets/homerr.gif'))
                await client.get_user(myAuthorId).send(zename + " a bon au Challenge " + str(current_challenge))
                await client.get_user(brice_identifiant).send(zename + " a bon au Challenge " + str(current_challenge))
                mytime = datetime.now()
                xdebut_time = 00
                xfinal_time = 5
                if xdebut_time <= mytime.hour <= xfinal_time :
                    print ('heure! :', mytime.hour)#debug
                    await message.channel.send('Vos points ont été doublés')
                    await client.get_user(myAuthorId).send(zename + " points doublé au Challenge " + str(current_challenge))
                    await client.get_user(brice_identifiant).send(zename + " points doublé au Challenge " + str(current_challenge))
                else :#commentable
                    print ('elseheure :', mytime)#debug commentable
            #si l'utilisateur a déjà participé  #affiche quand même mauvaise réponse
            if zename in block_it and thisisuniq == 1 :
                await message.channel.send('Vous êtes limité à une participation pour ce Challenge!!')
                if message.content.casefold() == listchallenger[current_challenge-1].casefold() : # voir si mettre en prod
                    await message.channel.send('Vous avez bon mais c\'est trop tard')
            if len(top3NamesQY) > 3 :
                await message.channel.send(repbotlate1)
                await message.channel.send(repbotlate1bis)
                ontBonMaisTropTardQY.append(zename) #sinon bug si refacto
            
            if message.content.casefold() == listchallengerx.casefold() and reptricheur(top3NamesQY, listchallengerx, message) != True :
            #     await message.channel.send(homer)      
                truc = None#cette fonction sert à n'envoyer que si c'est la mauvaise réponseet ou l'utilisateur reparticipe 
            elif zename in top3NamesQY : # cette fonction permet de ne pas afficher de message au tricheur et évite le else
                arretedeparticiper = None #arretedeparticiper bordel permet d'utiliser cette fonction
            else :
                perdu_images = ['./assets/perdu.gif', './assets/ohno.gif', './assets/ohnoo.gif']
                perdu_counter += 1
                await message.channel.send('Mauvaise réponse') 
                block_it.append(zename)
                perduAnImporteQuelQY.append(zename)
                # await message.channel.send(file=discord.File(random.choice(perdu_images)))
                if perdu_counter in (1, 3, 5, 8, 9, 11, 13, 15, 16, 18, 20, 25, 26, 29, 30, 33 , 35, 39, 41, 43, 45, 47, 49, 50, 55, 60, 65, 67, 78, 85, 90, 95, 100, 105, 107, 108, 109,\
                     111, 113, 115, 121, 123, 125, 127, 129, 130, 135, 140, 145, 150, 165, 175, 184, 190, 195, 200, 201, 202, 203, 204) : 
                    await message.channel.send(file=discord.File(random.choice(perdu_images)))


            print ("nbQxgagnant, top3NamesQY, ontBonMaisTropTardQY,  perduAnImporteQuelQY", "totdico")
            print (len(top3NamesQY), top3NamesQY, ontBonMaisTropTardQY, perduAnImporteQuelQY, totdico)

        # Dans le channel général et si c'est moi/Augustin bientôt        
        # elif zename == myAuthorId:
        elif zename == 'AMINE AA' :
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
        elif message.channel.id != my_channel_id :#commentable
            return#commentable
        # Tous les autres cas
        else :
            print ("Tous les autres cas :", message.content)
            # await message.add_reaction(emoji = '\N{THUMBS DOWN SIGN}')
    except (RuntimeError) :
        print ("Une erreur est survenue...Fermeture")
        sys.exit(1)        

# @client.event
# async def on_reaction_add(reaction, user):
    
# @bot.command(pass_context=True)
# async def checkreacts(ctx):
#     msg1 = await bot.say("React to me!")
#     custom_emoji = get(ctx.message.server.emojis, name="custom_emoji")
#     reaction = await bot.wait_for_reaction(['\N{SMILE}', custom_emoji], msg1)
#     await bot.say("You responded with {}".format(reaction.emoji))
client.run(token[0])
