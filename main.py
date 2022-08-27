import random

allcard=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
playercard=[]
computercard=[]
#發牌


def sortcard(card):
    now=[]
    for i in card:
        now.append(i%13+1)
    now.sort()
    return now
def randTF():   
    return random.choice([True,False])    
def fakecard():
    return random.randint(1,13)
def playersturn():
    global playercard
    global allcard
    global computercard
    playercard.sort()
    print(f"你現在的手牌有{playercard}")
    playercardin1=input("請輸入你要出的第一張牌")
    playercardin2=input("請輸入你要出的第二張牌")
    try:
        p=[]
        p=playercard.copy()
        p.remove(int(playercardin1))
        p.remove(int(playercardin2))
        allcard.append(int(playercardin1))
        allcard.append(int(playercardin2))
        print(f"你現在的手牌有{p}")
    except:
        print("你的手牌不足請重新輸入")
        playersturn()
    playercard=p
    lieornot=input("請問是否要說謊?(Y/N):")
    if randTF():
        if lieornot=="Y":
            playercard+=allcard
            print("你被抓到了")
        if lieornot=="N":
            computercard+=allcard
            print("電腦抓錯了")
        allcard=[]
    else:
        print("電腦不抓")
    print(f'目前剩下牌數:\n電腦:{len(computercard)}\n自己:{len(playercard)}\n場中:{len(allcard)}')
def computersturn():
    global playercard
    global allcard
    global computercard
    now = random.sample(computercard,2)
    for card in now:
        computercard.remove(card)
        allcard.append(card)
    print(f'電腦出的牌是{now}')
    lieornot=randTF()
    playcatchornot=input("請問是否要抓?(Y/N):")
    if playcatchornot=="Y":
        if not lieornot:
            playercard+=allcard
            print("抓失敗了")
        if lieornot:
            computercard+=allcard
            print("抓成功了")
        allcard=[]
    print(f'目前剩下牌數:\n電腦:{len(computercard)}\n自己:{len(playercard)}\n場中:{len(allcard)}')
def endornot():
    if  len(playercard)==0 or len(computercard)==0:
        return(False)
    else:
        return(True)



random.shuffle(allcard)
playercard=allcard[:26]
computercard=allcard[26:]
allcard=[]
playercard = sortcard(playercard)
computercard= sortcard(computercard)

while endornot():
    playersturn()
    if not endornot():
        break
    computersturn()
if len(computercard)==0:
    print("電腦獲勝")
else:
    print("玩家獲勝")
