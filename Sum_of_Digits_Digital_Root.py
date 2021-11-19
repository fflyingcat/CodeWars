def digital_root(n):
    l=len(str(n))
    sum=0
    while(l>1):
        for i in range(0,l):
            sum+=int(str(n)[i])
        n=sum
        sum=0
        l=len(str(n))
    return n

#https://www.codewars.com/kata/541c8630095125aba6000c00