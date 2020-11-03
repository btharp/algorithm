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
from pythonds.basic import Stack

rStack=Stack()

def toStr2(n,base):
    convertString="0123456789ABCDEF"
    while n>0:
        if n<base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n%base])
        n=n//base 

    res=""
    while not rStack.isEmpty():
        res=res+str(rStack.pop())
    return res 


# %%
print(toStr2(1453,16))




# %% Recursion Visualization
# Turtle 
import turtle 
myTurtle=turtle.Turtle()
myWin=turtle.Screen()
def drawSpriral(myTurtle,lineLen):
    if lineLen>0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpriral(myTurtle,lineLen-5)

drawSpriral(myTurtle,100)
myWin.exitonclick()


# %%
import turtle 
def tree(branchLen,t):
    if branchLen>5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t=turtle.Turtle() 
    myWin=turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()
main()


# %%  Sierpinski Triangle
import turtle 
def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def sierpinski(points,degree, myTurtle):
    colormap=['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree>0:
        sierpinski([points[0],getMid(points[0],points[1]),getMid(points[0],points[2])],
                    degree-1,myTurtle)
        sierpinski([points[1],getMid(points[0],points[1]),getMid(points[1],points[2])],
                    degree-1,myTurtle)
        sierpinski([points[2],getMid(points[2],points[1]),getMid(points[0],points[2])],
                    degree-1,myTurtle)   

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,5,myTurtle)
   myWin.exitonclick()

main() 








# %% Dynamic Programming
def recMc(coinValueList,change):
    minCoins=change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMc(coinValueList,change-i)
            if numCoins<minCoins:
                minCoins=numCoins
    return minCoins 

#%%
print(recMc([1,5,10,25],63))

# %%
