# Project Euler #4: Largest palindrome product

import sys

def isPalindrome(n):
    temp=n
    rev=0
    while(n>0):
        rev=rev*10 + n%10
        n//=10
    return rev==temp

def largestPrime(n):
    res=0
    for i in range(990,99,-11):
        for j in range(999,99,-1):
            prod=i*j
            if(res<prod<n and isPalindrome(prod)):
                res=prod
                break
            elif(prod<res):
                break
    return res
t=int(input())
for i in range(t):
    N=int(input())
    print(largestPrime(N))