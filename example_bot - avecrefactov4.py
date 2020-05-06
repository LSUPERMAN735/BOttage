#!/usr/bin/env python3
# -- coding: utf-8 --
#4may and 5 may and 6may 

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

# global nbQ1Wins

top10IdsQ1 = []
top10IdsQ2 = []
# nbQ1Wins = len(top10IdsQ1)
# nbQ2Wins = len(top10IdsQ2) #ne fonctionne pas
winningQ1ButLateIds = []
winningQ2ButLateIds = []
looseAtAllIds = []

#answer challenge 
answer1='1) Linux Mint'
answer2='2) Google Images -> Insérer image -> Rechercher'

#bot answer
wonfisrtpart='Vous avez gagné à la question'
#bot answer
homer='Homer: Woohoo!! Vous êtes trop fort!!'
# answer if try to cheat:
answercheat1='Vous avez déjà participé ! Faîtes autre chose !!'
answercheat2='tente de triche!!'

#answer where too late by bot
answerbotlate1='Désolé mais 10 autres personnes ont déjà gagné'
answerbotlate1bis='Soyez plus rapide à la prochaine question '

####
# Events
####
client = commands.Bot(command_prefix='.')


#def of functions 
def answerifcheat(top10IdsQx, answerx, msg):
    if msg.author.id in top10IdsQx and msg.content.casefold()== answerx.casefold() :
        msg.channel.send(answercheat1) # awar async ne fonctionne pas sur la fonction
        print(msg.author.id, answercheat2)
        return False # value that block the questionsX where we are trying to cheat
    else: 
        return True

def reply_question(msg, repx, top10IdsQx, winningQxButLateIds, Qx):
    if msg.content.casefold() ==repx.casefold() and answerifcheat(top10IdsQx, repx, msg)==True:
        # msg.channel.send(wonfirstq)# await 
        print(wonfisrtpart,Qx)
        print(msg.author.id)
        top10IdsQx.append(msg.author.id)
        print('gagné', Qx, '=', len(top10IdsQx))
        print('gagné', Qx, 'mais late =', len(winningQxButLateIds))
        return True

@client.event
async def on_ready():
    print ('Challenge Bot est prêt.')
    return True        

@client.event
async def on_message(message):
    try:
        # global appel_membre, appel, absents, presents

        global top10IdsQ1, top10IdsQ2, winningQ1ButLateIds, winningQ2ButLateIds, looseAtAllIds

        if message.author.id != BOTman_id:
            print("Je suis", message.author.id)
            print("current state is")
            print("my_channel_id, BOTman_id, myAuthorId", \
                my_channel_id, BOTman_id, myAuthorId)
            print("nbQ1Wins, nbQ2Wins, top10IdsQ1,top10IdsQ2, winningQ1ButLateIds, winningQ2ButLateIds, looseAtAllIds")
            print(len(top10IdsQ1), len(top10IdsQ2), top10IdsQ1, top10IdsQ2, winningQ1ButLateIds, winningQ2ButLateIds, looseAtAllIds)
            print("Message initial", message)

        # High Priviledged people, for starting challenge (in any channel)
        if message.content == 'Challenge!!' \
            and message.author.id in (myAuthorId, brice_Id, admin_Id) :
            await message.channel.send('coucou Challenge 1 : Savez-vous comment s appelle mon logo')
            await message.channel.send('Si non faites un reverse search sur Google ou BING ')
            await message.channel.send('Réponse sous la forme : en MP')
            await message.channel.send('1) Google Chrome //ne pas oublier le numéro la parenthèse et l espace et majuscule')
        elif message.content == '!!Challenge' \
            and message.author.id in (myAuthorId, brice_Id, admin_Id) :    
            await message.channel.send('Challenge 2 : Comment faire le reverse search ?')
            await message.channel.send('Réponse sous la forme : en MP')
            await message.channel.send('2) Google Chrome -> Téléchargement -> Cliquer sur le fichier téléchargé //ne pas oublier le numéro la parenthèse et l espace et majuscule')
        
        # In private channel and it is not the bot
        if isinstance(message.channel, discord.DMChannel) and message.author.id != BOTman_id:
            print("Message privé : " + message.content)

            if answerifcheat(top10IdsQ1, answer1, message)!=True:
                await message.channel.send(answercheat1) 

            # reply_question(message, answer1, top10IdsQ1, nbQ1Wins, winningQ1ButLateIds)
            # reply_question(message, answer2, top10IdsQ2,  nbQ2Wins, winningQ2ButLateIds)
            if reply_question(message, answer1, top10IdsQ1, winningQ1ButLateIds,'Q1') == True :
                await message.channel.send(wonfisrtpart+' 1')
            
            if len(top10IdsQ1) > 10:
                await message.channel.send(answerbotlate1)
                await message.channel.send(answerbotlate1bis)
                winningQ1ButLateIds.append(message.author.id) #sinon bug

            if message.content.casefold()==answer1.casefold() and answerifcheat(top10IdsQ1, answer1,  message)!=True :
                await message.channel.send(homer) 

            elif answerifcheat(top10IdsQ2, answer2, message)!=True:
                await message.channel.send(answercheat1) 
            elif reply_question(message, answer2, top10IdsQ2, winningQ2ButLateIds,'Q2') == True :
                await message.channel.send(wonfisrtpart+' 2')
                
                if len(top10IdsQ2) > 10:
                    await message.channel.send(answerbotlate1)
                    await message.channel.send(answerbotlate1bis)
                    winningQ2ButLateIds.append(message.author.id) #sinon bug
                
                if message.content.casefold()==answer2.casefold() and answerifcheat(top10IdsQ2, answer2, message)!=True :
                    await message.channel.send(homer) 
                    # print('gagné ', Qx, ' =', len(top10IdsQ2))
                    # print('gagné ', Qx, ' mais late=', len(winningQ2ButLateIds))
            else:
                await message.channel.send('Désolé vous avez perdu') 
                looseAtAllIds.append(message.author.id)

        # In general channel and it is mySelf        
        # elif message.author.id == myAuthorId:
        elif message.author.name == 'AMINE AA':
            print("My message in general channel :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS UP SIGN}') 
        #if it's the bot
        elif not isinstance(message.channel, discord.DMChannel) and message.author.id ==BOTman_id:
            print("BOT messaged in general channel :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS UP SIGN}')
        
        # In general channel and anyone other than myself
        elif not isinstance(message.channel, discord.DMChannel):
            print("Someone messaged in general channel :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS DOWN SIGN}')
        # Bot message    
        elif message.author.id == BOTman_id:
            print("Message du bot :", message.content)
        #if the channel is not my channel or of the teacher by Augustin
        elif message.channel.id != my_channel_id:
            return
        # Unhandled case
        else:
            print("Unhandled case :", message.content)
            await message.add_reaction(emoji = '\N{THUMBS DOWN SIGN}')
    except (RuntimeError):
        print("Error caught...exiting")
        sys.exit(1)        

client.run(token[0])
