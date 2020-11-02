#%%
def listsum(numlist):
    theSum=0
    for i in range(len(numlist)):
        theSum+=numlist[i]
    
    return theSum
# %%
print(listsum([1,3,5,7,9]))


# %%  Sum with recursion
def listsum2(numlist):
    if len(numlist)==1:
        return numlist[0]
    else:
        return numlist[0]+listsum2(numlist[1:])
    
# %%
print(listsum2([i for i in range(100)]))
# %%
import sys
sys.setrecursionlimit(1000000)


# %% convert an integer to a string in any base
def toStr(n,base):
    convertString="0123456789ABCDEF"
    if n<base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base]


# %%
print(toStr(1453,16))
# %%
