# Project Euler #3: Largest prime factor

import sys
import math
# prime factorization
def largestPrime(n): 
    maxPrime=-1
    #removing even factors
    while(n%2==0): 
        maxPrime=2
        n//=2
    #iterating over odd factors for largest factor
    for i in range(3,int(math.sqrt(n))+1,2): 
        while(n%i==0): 
            maxPrime=i 
            n//=i 
    if(n>2):
        return n
    else:
        return maxPrime
t = int(input())
for i in range(t):
    N = int(input())
    print(largestPrime(N))