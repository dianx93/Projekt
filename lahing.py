from random import *
from database import *
from map import delfrommap
from aken import LEFT,RIGHT,DOWN,UP

def lahing(tegevus,char):                #monster=number
    #mon=char.uuskoletis(monster)
    if tegevus=='a':
        ca=randint(char.W.mindam,char.W.maxdam)+char.boonus
        char.boonus=0
        if randint(0,100/char.W.crit)==0:      #crit
            ca*=2
        if randint(0,1)==0:                 #koletis ründab
            ma=randint(0,char.M.attack)
            if ca>ma:
                char.M.hp-=ca-ma
            elif ma>ca:
                char.hp-=ma-ca
            else:
                print('You both attack with equal force!')
        else:                               #koletis kaitseb
            ma=randint(0,char.M.defence)
            if ca>ma:
                char.M.hp-=ca-ma
            else:
                print('Monster defended successfully!')
    elif tegevus=='d':
        char.boonus+=char.A.defence
        if randint(0,1)==1:                 #koletis kaitseb
            print('None of you are brave enough to attack.')
        else:                               #koletis ründab
            ca=randint(0,char.A.defence)
            ma=randint(0,char.M.attack)
            if ma>ca:
                char.hp-=ma-ca
            else:
                print('You defended successfully!')
    if char.M.hp<=0:
        print("The",char.M.name,"is DEAD!")    #lahing over
        delfrommap(char.M.location[0],char.M.location[1])
        char.uuskoletis(0)
        char.battle=False
        #koletis kustub kaardilt
    if char.hp<=0:
        print("You are DEAD!")              #GAME OVER
        
    print("koletise elud",char.M.hp)           #lahingu kontroll...
    print("sinu elud",char.hp)              #lahingu kontroll...
