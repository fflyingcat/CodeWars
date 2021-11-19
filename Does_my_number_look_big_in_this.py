import math

def narcissistic( value ):
    n = len(str(value))
    val=str(value)
    check = 0
    for i in range (0,n):
        check+=(math.pow(int(val[i]),n))
    if (check==value):
        return True
    else:
        return False
#https://www.codewars.com/kata/5287e858c6b5a9678200083c