# Project Euler #5: Smallest multiple
import sys
import math
def smallestMultiple(n):
    p=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    sqrt_n=math.sqrt(n)
    log_n=math.log(n)
    res=1
    i=0
    while(p[i]<=sqrt_n):
        res*= (p[i]**(math.floor(log_n/math.log(p[i]))))
        i+=1
    
    while(p[i]<=n):
        res*=p[i]
        i+=1
    return int(res)
t=int(input())
for i in range(t):
    N=int(input())
    print(smallestMultiple(N))