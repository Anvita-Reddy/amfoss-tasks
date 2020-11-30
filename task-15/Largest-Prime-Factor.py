'''
Project Euler #3: Largest prime factor

The prime factors of  13195 are 5,7,13 and 29.
What is the largest prime factor of a given number N?

Input Format

First line contains T, the number of test cases.
This is followed by T lines each containing an integer N.

Constraints

1 ≤ T ≤ 10
10 ≤ N ≤ 10^12

Output Format

For each test case, display the largest prime factor of N.

Sample Input 0

2
10
17

Sample Output 0

5
17

Explanation 0

Prime factors of 10 are {2,5}, largest is 5.
Prime factor of 17 is 17 itself, hence largest is 17.
'''

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