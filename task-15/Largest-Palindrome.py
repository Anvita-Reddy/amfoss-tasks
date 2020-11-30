'''
Project Euler #4: Largest palindrome product

A palindromic number reads the same both ways.
The smallest 6 digit palindrome made from the product of two 3-digit numbers is 101101 = 143 x 707
Find the largest palindrome made from the product of two 3-digit numbers which is less than N.

Input Format
First line contains T that denotes the number of test cases.
This is followed by T lines, each containing an integer, N.

Constraints

1 ≤ T ≤ 100
101101 < N < 1000000

Output Format

Print the required answer for each test case in a new line.

Sample Input 0

2
101110
800000

Sample Output 0

101101
793397

Explanation 0

101101 is product of 143 and 707.
793397 is product of 869 and 913.

'''
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