'''
Is This JEE 

Everyone loves short problem statements.
Given a function f(x) find its minimum value over the range 0 < x < π/2

f(x)=(x^2+b*x+c)/sin(x)

Input:
First-line will contain T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, two real numbers b,c.

Output:
For each test case, output the minimum value of f(x) over the given range.
Absolute error of 10^6 is allowed.

Constraints:
1 ≤ T ≤ 100000
1 ≤ b,c ≤ 20

Sample Input:
1
2 2

Sample Output:
5.8831725615
'''

import math
def func(x,b,c):
    return(x*x + b*x + c)/(math.sin(x))
try:
    T=int(input())
    for i in range(T):
        b,c=map(int,input().split())
        res=func(0.1,b,c)
        i=0.1
        while(i<1.57):
            res=min(res,func(i,b,c))
            i+=0.1
        print(res)
except BaseException:
    pass