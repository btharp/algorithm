#%%
210//11
# %%
def hash(astring,tablesize):
    sum=0
    for pos in range(len(astring)):
        sum+=ord(astring[pos])
    return sum%tablesize
# %%
hash("cat",11)

# %% Bubble Sorting
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp 
    

# %%
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


# %% Short Bubble: stop early
def shortBubbleSort(alist):
    exchange=True
    passnum=len(alist)-1
    while passnum>0 and exchange:
        exchange=False 
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchange=True 
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp 
        passnum=passnum-1

alist = [54,26,93,17,77,31,44,55,20]
shortBubbleSort(alist)  
print(alist)





# %%  Selection Sort
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionofMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionofMax]:
                positionofMax=location
            
        temp=alist[fillslot]
        alist[fillslot]=alist[positionofMax]
        alist[positionofMax]=temp 
    return alist 

# %%
alist = [54,26,93,17,77,31,44,55,20]
print(selectionSort(alist))


# %%  Insertion Sort 
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue=alist[index]
        position=index 

        while position>0 and list[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position=position-1
        
        alist[position]=currentvalue 


#%% Shell Sort 
