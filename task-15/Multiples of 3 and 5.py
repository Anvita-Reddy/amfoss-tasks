# Project Euler #1: Multiples of 3 and 5

#!/bin/python3

import sys

def findSum(a,n):
    return a*(((n//a)*(n//a+1))//2)

t=int(input())
for i in range(t):
    s3,s5,s15=0,0,0
    n=int(input())
    if(n%3==0):
        s3=findSum(3,n-3)
    else:
        s3=findSum(3,n)
    if(n%5==0):
        s5=findSum(5,n-5)
    else:
        s5=findSum(5,n)
    if(n%15==0):
        s15=findSum(15,n-15)
    else:
        s15=findSum(15,n)
    print(s3+s5-s15)
