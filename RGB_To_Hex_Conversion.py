import math

def tohex(x):
    stack = []
    if (x==0 or x<0):
        stack.append("0")
    if(x>255):
        x=255
    while (x > 0):
        if (math.floor(x % 16) == 0):
            stack.append("0")
        if (math.floor(x % 16) == 1):
            stack.append("1")
        if (math.floor(x % 16) == 2):
            stack.append("2")
        if (math.floor(x % 16) == 3):
            stack.append("3")
        if (math.floor(x % 16) == 4):
            stack.append("4")
        if (math.floor(x % 16) == 5):
            stack.append("5")
        if (math.floor(x % 16) == 6):
            stack.append("6")
        if (math.floor(x % 16) == 7):
            stack.append("7")
        if (math.floor(x % 16)== 8):
            stack.append("8")
        if (math.floor(x % 16) == 9):
            stack.append("9")
        if (math.floor(x % 16) == 10):
            stack.append("A")
        if (math.floor(x % 16) == 11):
            stack.append("B")
        if (math.floor(x % 16) == 12):
            stack.append("C")
        if (math.floor(x % 16) == 13):
            stack.append("D")
        if (math.floor(x % 16) == 14):
            stack.append("E")
        if (math.floor(x % 16) == 15):
            stack.append("F")
        x = math.floor(x / 16)

    res=""
    if(len(stack)==1):
        stack.append("0")
    while(len(stack)>0):
        res+=stack.pop()
    return res

def rgb(r, g, b):
    return(tohex(r)+tohex(g)+tohex(b))
#https://www.codewars.com/kata/513e08acc600c94f01000001