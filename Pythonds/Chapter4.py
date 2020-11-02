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
# %%
