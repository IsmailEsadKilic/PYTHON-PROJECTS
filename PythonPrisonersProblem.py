# veritasiumsu agamsı
import random


def genrandboxtoslip(lim):
    sliplist = [ a for a in range(1, lim + 1)]
    random.shuffle(sliplist)
    dadict = {}
    for numero in range(1, lim + 1):
        dadict[numero] = sliplist.pop(0)
    return dadict



def letryforprisno(iter,no,dadict):
    checking = no
    tryno = 1
    while tryno < 51:
        result = dadict[checking]
        print(f"universe {iter} prisoner {no} is checked box no {checking} and found slip no {result}")
        if result == no:
            print(f"universe {iter} prisoner {no} has found its new host!")
            return True
        else:
            checking = result
            tryno += 1
    return False

def ite(iterno,pricount):
    dadict = genrandboxtoslip(pricount)
    for prisonerno in range(1,pricount+1):
        tried = letryforprisno(iterno,prisonerno,dadict)
        if tried == False:
            return False
    return True

def maain(pricount):
    success = 0
    for i in range(1,500):
        wha = ite(i,pricount)
        if wha == True:
            success += 1
        print(f"SUCCESS RATE IS = {success/i*100}% percent")

maain(100)

#sparkle in my heart,
#wonder in your world