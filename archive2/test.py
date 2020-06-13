#!/usr/bin/env python3
# -- coding: utf-8 --
#panada avec head ?
fichdeqr = open("myq.txt", "r")
lignes = fichdeqr.readlines()
a=0
# lignes
# ['girafe\n', 'tigre\n', 'singe\n', 'souris\n']
for q in lignes:
    a+=1
    delims=q.split('|')
    quest=delims[0]
    rep=delims[1]
    # print(quest)
    # print(rep)
    # print(a)
    # print(q)#à ne pas faire
# print(quest)
fichdeqr.close()
