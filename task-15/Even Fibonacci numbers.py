# Project Euler #2: Even Fibonacci numbers
#!/bin/python3

import sys

def fibonacci(n):
    a,b=0,1
    res=[]
    while(b<n):
        res.append(b)
        a,b=b,a+b
    del res[0]
    return res

t=int(input())
for i in range(t):
    N=int(input())
    nums=fibonacci(N)
    c=0
    for i in nums:
        if((i%10)%2==0):
            c+=i
    print(c)
