'''
Project Euler #1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.

Input Format

First line contains T that denotes the number of test cases.
This is followed by T lines, each containing an integer, N.

Constraints

1 ≤ T ≤ 10^5
1 ≤ N ≤ 10^9

Output Format

For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.

Sample Input 0

2
10
100

Sample Output 0

23
2318

Explanation 0
For N=10, if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9.
The sum of these multiples is 23.
Similarly for N=100, we get 2318.
'''

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