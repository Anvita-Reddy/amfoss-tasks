'''
HomeWork Time
Since Elastic Girl got her new superhero job, it is now Mr.Incredible's job
to take care of the kids. Dash is very fast running but he finds it difficult
to keep up the same speed when it comes to solving maths problems.
He gets a homework problem everyday.
Knowing that Dash faces difficulties in solving mathematical problems Mr.Incredible does the homework.
Today Dash was asked to print the reverse of the n'th number in the Incredible series.
In the incredible series the n'th number i.e F(n) is equal to the sum of F(n-1),F(n-2),F(n-3) modulo (10^9 + 7).
i.e in short F(n) = (F(n-1) + F(n-2) + F(n-3))%(10^9 + 7).
The first three numbers in the series are 1, 2, 3.
While printing the reverse of a number print the number without leading zeroes.
Ex: If the n'th Incredible number is 11200 then it's reverse is not 00211 it is 211.
It has been quite a time since Mr.Incredible did maths and moreover he has trouble babysitting Jack-Jack.
So Mr.Incredible wants you to solve the problem for him.

Input Format

First line of the input contains a single integer T, number of test cases. Then test cases follow.

Each test case contains a single line of input, integer n.

Constraints

1<=T<=1000

1<=n<=1000000

Output Format

For each test case, output a single line containing the reverse of the n-th number of the incredible series(excluding leading zeros).

Sample Input 0

3
10
12
5

Sample Output 0

32
877
11

Explanation 0

The Incredible series is 1,2,3,6,11,20,37,68,125,230 and so on...
The 10'th Incredible number is 230. It's reverse without any leading zeroes is 32
The 12'th Incredible number is 778. It's reverse without any leading zeroes is 877
The 5'th Incredible number is 11. It's reverse without any leading zeroes is 11 itself

'''
def inc(n):
    m=(10**9+7)
    a,b,c=1,2,3
    if(n<4):
        return n
    else:
        i=4
        while(True):
            curr=(( (a+b) %m) +c )%m
            a,b,c=b,c,curr
            if(i==n):
                return curr
            i+=1
            
def reversing():
    p=inc(int(input()))
    return int(str(p)[::-1])

t=int(input())
for i in range(t):
    print(reversing())