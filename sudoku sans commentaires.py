 #Programme dérivé de projet d'ISN par Alexis Chatelain en classe de TS1 au lycée Vinci d'Amboise 2018-2019.
from random import randint
import random

def declaration_grille():
    global ok,grille,grille_ref,grille_save
    grille=[[123456789 for i in range(9)]for i in range(9)]

def generation_sudoku():
    global x,y,Var,ok,msg,hist1,hist2,hist3,hist4
    ok=0
    while ok!=27:
        for i in range(9):
            for j in range(9):
                if grille[i][j] == "" or grille[i][j] == "0"  or grille[i][j] == 0:
                    declaration_grille()
        verif()
        trouver()
        ok2=0
        for i in range(9):
            for j in range(9):
                if grille[i][j] > 9:
                    x=i
                    y=j
                    ok2=1
                    break
            if ok2==1:
                break
        Var=str(randint(1,9))
        if str(grille[x][y]).count(Var) > 0:
            ecrire()
    ok=0
    return (grille)
	
def trouver():
    global x,y,x1,y1,Var,ok1
    ok1=0
    for i in range(9):
        for j in range(9):
            if grille[i][j] < 10 :
                x=i
                y=j
                Var=str(grille[i][j])
                ecrire()
                if ok1==1:
                    trouver()
    x1=y1=cherche=cherche1=cherche2=cherche3=cherche4=cherche5=cherche6=0
    for i in range(9):
        for j in range(9):
            if grille[i][j] < 100 and grille[i][j] > 9 :
                x1=i
                y1=j
                for k in range(9):
                    if str(grille[x1][k]).count(str(str(grille[x1][y1])[:1]))!=0:
                        cherche=1
                for k in range(9):
                    if str(grille[k][y1]).count(str(str(grille[x1][y1])[:1]))!=0:
                        cherche2=1
                a=int(x/3)*3
                b=a+3
                c=int(y/3)*3
                d=c+3
                for i in range(a,b):
                    for j in range(c,d):
                        if str(grille[x1][y1]).count(str(str(grille[x1][y1])[:1]))!=0:
                            cherche3=1
                for k in range(9):
                    if str(grille[x1][k]).count(str(str(grille[x1][y1])[-1:]))!=0:
                        cherche4=1
                for k in range(9):
                    if str(grille[k][y1]).count(str(str(grille[x1][y1])[-1:]))!=0:
                        cherche5=1
                a=int(x/3)*3
                b=a+3
                c=int(y/3)*3
                d=c+3
                for i in range(a,b):
                    for j in range(c,d):
                        if str(grille[x1][y1]).count(str(str(grille[x1][y1])[-1:]))!=0:
                            cherche6=1
                if cherche==1 or cherche2==1 or cherche3==1:
                    Var = str(str(grille[x1][y1])[:1])
                elif cherche4==1 or cherche5==1 or cherche6==1:
                    Var = str(str(grille[x1][y1])[-1:])
                else:
                    alea=randint(1,2)
                    if alea == 1:
                        Var = str(str(grille[x1][y1])[:1])
                    else:
                        Var = str(str(grille[x1][y1])[-1:])
                x=x1
                y=y1
                ecrire()
                trouver()
    for i in range(9):
        for j in range(9):
            if grille[i][j] < 100 and grille[i][j] > 9 :
                trouver()

def ecrire():
    global ok1,Var,x2, y2
    ok3=0
    for i in range(9):
        for j in range(9):
            if str(grille[i][j]) == "" or str(grille[i][j]) == "0"  or grille[i][j] == 0:
                declaration_grille()
                ok3=1
                break
        if ok3==1:
            break
    ok1 = 0
    grille[x][y] = int(Var)
    for i in range(9):
        if i != x:
            x2=i
            y2=y
            rengaine()
    for j in range(9):
        if j != y:
            x2=x
            y2=j
            rengaine()
    a=int(x/3)*3
    b=a+3
    c=int(y/3)*3
    d=c+3
    for i in range(a,b):
        for j in range(c,d):
            if i!= x and j!=y:
                x2=i
                y2=j
                rengaine()

def rengaine():
    global ok1
    if str(grille[x2][y2]).count(Var) > 0:
        var2=str(grille[x2][y2]).find(Var)+1
        if str(grille[x2][y2])[-(len(str(grille[x2][y2]))-var2):]==str(grille[x2][y2]):
            try:
                grille[x2][y2]=int(str(str(grille[x2][y2])[:var2-1]))
            except ValueError:
                declaration_grille()
        else:
            grille[x2][y2]=int(str(grille[x2][y2])[:var2-1] + str(grille[x2][y2])[-(len(str(grille[x2][y2]))-var2):])
        ok1 =1

def verif():
    global ok
    a=0
    b=3
    c=0
    d=3
    ok=0
    somme=0
    for i in range(9):
        for j in range(9):
            if grille[i][j] != "" and grille[i][j]<10  :
                somme = somme + int(grille[i][j])
        if somme == 45:
            ok=ok+1
        somme= 0
    for j in range(9):
        for i in range(9):
            if grille[i][j] != "" and grille[i][j]<10  :
                somme = somme + int(grille[i][j])
        if somme == 45:
            ok=ok+1
        somme= 0
    for e in range (3):
        for z in range(3):
            for i in range(a,b):
                for j in range(c,d):
                    if grille[i][j] != "" and grille[i][j]<10  :
                        somme = somme + int(grille[i][j])
            if somme == 45:
                ok=ok+1
            somme= 0
            c=c+3
            d=d+3
        a=a+3
        b=b+3
        c=0
        d=3

declaration_grille()
grille=generation_sudoku()
for i in range(9):
            for j in range(9):
                print(grille[i][j]);