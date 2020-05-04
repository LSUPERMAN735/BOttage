#!/usr/bin/env python3
# -- coding: utf-8 --
#panada avec head ?
fichdeqr = open("myq.txt", "r")
lignes = fichdeqr.readlines()
# lignes
# ['girafe\n', 'tigre\n', 'singe\n', 'souris\n']
for q in lignes:
    delims=q.split('|')
    quest=delims[0]
    rep=delims[1]
    print(quest)
    print(rep)
    # print (head[0])
    # print(q)
fichdeqr.close()