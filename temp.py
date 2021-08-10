import random
import sys
psymbol,csymbol ="X","O"
bottomline = "-"*10
validpos = [" "]*10
poslist = list(range(1,10))
userlist,pclist = [], []

playername = input("Enter player 1 name[X]: ")
playertwoname = input("Enter player 2 name[O]: ")
# Common fx
def printsampletable():
    j = 1
    while(j<10):
        print(j,end=" | ")
        print(j+1,end=" | ")
        print(j+2)
        print(bottomline)
        j+=3

def visrep():
    i = 0
    while(i<9):
        print(validpos[i],end=" | ")
        print(validpos[i+1],end=" | ")
        print(validpos[i+2])
        print(bottomline)
        i+=3  

# player 1 fx
def posinputpone():
    temppos = input(playername+" enter position(1-9): ")
    if temppos == "mark":
        pcturnpone()
    elif temppos == "quit":
        sys.exit(playertwoname+" WON")
    elif int(temppos) in poslist:
        updatepos(int(temppos))
    else:
        print("Enter a valid position!")
        posinputpone()

def updatepos(pos):
    userlist.append(pos)
    poslist.remove(pos)
    validpos[pos-1] = psymbol 

def pcturnpone():
    pos = random.choice(poslist)
    updatepos(pos)

def wincheckpone():
    if 1 in userlist and 2 in userlist and 3 in userlist:
        return True
    elif 4 in userlist and 5 in userlist and 6 in userlist:
        return True
    elif 7 in userlist and 8 in userlist and 9 in userlist:
        return True
    elif 1 in userlist and 4 in userlist and 7 in userlist:
        return True
    elif 2 in userlist and 5 in userlist and 8 in userlist:
        return True
    elif 4 in userlist and 6 in userlist and 9 in userlist:
        return True
    elif 1 in userlist and 5 in userlist and 9 in userlist:
        return True
    elif 3 in userlist and 5 in userlist and 7 in userlist:
        return True
    else:
        return False

# player 2 fx
def posinputptwo():
    temppos = (input(playertwoname+" enter position(1-9): "))
    if temppos =="mark":
        pcturnptwo()
    elif temppos == "quit":
        sys.exit(playername+" WON")
    elif int(temppos) in poslist:
        updatepospc(int(temppos))
    else:
        print("Enter a valid position!")
        posinputptwo()

def updatepospc(pos):
    pclist.append(pos)
    poslist.remove(pos)
    validpos[pos-1] = csymbol

def pcturnptwo():
    pos = random.choice(poslist)
    updatepospc(pos)

def wincheckptwo():
    if 1 in pclist and 2 in pclist and 3 in pclist:
        return True
    elif 4 in pclist and 5 in pclist and 6 in pclist:
        return True
    elif 7 in pclist and 8 in pclist and 9 in pclist:
        return True
    elif 1 in pclist and 4 in pclist and 7 in pclist:
        return True
    elif 2 in pclist and 5 in pclist and 8 in pclist:
        return True
    elif 4 in pclist and 6 in pclist and 9 in pclist:
        return True
    elif 1 in pclist and 5 in pclist and 9 in pclist:
        return True
    elif 3 in pclist and 5 in pclist and 7 in pclist:
        return True
    else:
        return False
def runprogram():
    printsampletable()
    resone , restwo = False, False
    count = 0
    while(len(poslist)>1):
        posinputpone()
        resone = wincheckpone()
        if resone == True:
            print(playername+" WON.")
            count = 1
        posinputptwo()
        restwo = wincheckptwo()
        if restwo == True:
            print(playertwoname+" WON.")
            count = 1
        visrep()
    if count == 1:
        playagain()
    posinputpone()
    visrep()
    resone = wincheckpone()
    if resone == True:
        print(playername+" WON.")
    else:
        print("It's a tie.Game Over!")
    playagain()

def playagain():
    consent = input("Do you want to play again(play/quit): ")
    if consent == "play":
        global validpos
        global poslist
        validpos = [" "]*10
        poslist = list(range(1,10))
        global userlist
        global pclist
        userlist, pclist = [], []
        runprogram()
    elif consent == "quit" :
        sys.exit("Exited.")
    else:
        print("Plese enter correct input.")
        playagain()

if __name__ == '__main__':
    runprogram()