#%% Decimal to Binary
from pythonds.basic import Stack
def divideBy2(decNumber):
    remstack=Stack()

    while decNumber>0:
        rem=decNumber%2 
        remstack.push(rem)
        decNumber=decNumber//2

    binString=""

    while not remstack.isEmpty():
        binString+=str(remstack.pop())
    
    return binString

print(divideBy2(233))
# %% Octal 
def divideBy8(decNumber):
    remstack=Stack()
    
    while decNumber>0:
        rem=decNumber%8
        remstack.push(rem)
        decNumber//=8

    OctString=""
    while not remstack.isEmpty():
        OctString+=str(remstack.pop())

    return OctString 

# %% 
divideBy8(25)


# %% Hexidecimal
def divideBy16(decNumber):
    remstack=Stack()

    while decNumber>0:
        rem=decNumber%16
        remstack.push(rem)
        decNumber//=16

    HexiString=""
    while not remstack.isEmpty():
        HexiString+=str(remstack.pop())

    return HexiString 

# %%
divideBy16(256)


# %% base26
def divideBy26(decNumber):
    remstack=Stack()

    while decNumber>0:
        rem=decNumber%26
        remstack.push(rem)
        decNumber//=26

    HexiString=""
    while not remstack.isEmpty():
        HexiString+=str(remstack.pop())

    return HexiString 
# %%
divideBy26(26)

# %%
def solution(s1,s2):
    
    ls1=len(s1)
    ls2=len(s2)

    if ls1!=ls2:
        return False 
    
    l1=[0]*26
    l2=[0]*26


    for i in range(ls1):
        pos=(ord(s1[i])-ord("a"))
        l1[pos]+=1
    
    for i in range(ls2):
        pos=ord(s2[i])-ord("a")
        l2[pos]+=1
    
    if l1==l2:
        return True 
    else:
        return False




# %%  Hot Potato
from pythonds.basic import Queue

def hotPotato(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()
# %%
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))


# %%  Printing Tasks
from pythonds.basic import Queue
import random 

class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm
        self.currentTask=None 
        self.timeRemaining=0

    def tick(self):
        if self.currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask=None 
    
    def busy(self):
        if self.currentTask!=None:
            return True 
        else:
            return False 
    
    def startNext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages()*60/self.pagerate 



class Task:
    def __init__(self,time):
        self.timestamp=time 
        self.pages=random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages 
    
    def waitTime(self,currenttime):
        return currenttime-self.timestamp 

def simulation(numSeconds,pagesPerMinute):

    labprinter=Printer(pagesPerMinute)
    printQueue=Queue()
    waitingtimes=[]

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task=Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask=printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)

    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
    num=random.randrange(1,181)
    if num==180:
        return True 
    else:
        return False 

for i in range(10):
    simulation(3600,5) 
    



# %%  Dequeue
# Palindrome-Checker 检测回文
from pythonds.basic import Deque
def PalChecker(aString):
    chardeque=Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEquall=True 

    while chardeque.size>1 and stillEquall:
        first=chardeque.removeFront()
        last=chardeque.removeRear() 
        if first!=last:
            stillEquall=False 

    return stillEquall 


# %%
