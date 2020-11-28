'''
Alex likes letters.
He loves the letter ‘D’.
He loves the letter ‘D’ especially when it comes embedded in crystals in a certain pattern.
A crystal of size n (n is odd and n > 1) is an n × n matrix made of ‘D’ and ‘*’.
You are given an odd integer n. Make a crystal of size n and print it.
Look at the examples to understand what you need to print.

Input Format

There is only input ‘n’ denoting the size of the crystal

Constraints

1 < n < 30

Output Format

Output the pattern of the crystal.

Sample Input 0

3

Sample Output 0

*D*
DDD
*D*

Sample Input 1

5

Sample Output 1

**D**
*DDD*
DDDDD
*DDD*
**D**

'''

n=int(input())
mid=n//2+1
for i in range(1,n+1):
    l=[]
    for j in range(0,abs(mid-i)):
        l.append('*')
    c=abs(n-2*abs(mid-i))
    for k in range(0,c):
        l.append('D')
    for j in range(0,abs(mid-i)):
        l.append('*')
    print(*l,sep="")