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
        return numlist[0]+listsum(numlist[1:])

# %%
print(listsum2([1,3,5,7,9]))
# %%
