'''
Jack Jack Codes

Jack Jack has just got his superpowers.
His parents have decided that it is high time for him to be enrolled in a Programming Course
so that he can use his superpowers for the betterment of Open Source.
Jack Jack unfortunately does not know how to code.
So help Jack Jack solve the following question.
Given an array of N integers.
Find out if there exists atleast a pair of elements such that the sum of the elements is equal to M.

Formally find out if there exist two indices i,j (i != j) such that array[i] + array[j] is equal to M. If there exists atleast one such pair print "True" else print "False"(without the quotes)

Input Format

The first line contains two integers N and M.

The second line contains N seperated integers denoting the values of the array

Constraints

2 <= N <= 10^5

The values of the array lie in the range [-10^7,10^7]

-10^8 <= M <= 10^8

Output Format

Output a single line containing "True" if there exists a pair. Else output "False".

Sample Input 0

4 10
4 8 2 6

Sample Output 0

True

Explanation 0

The pair [4,6] satisfies the condition (4 + 6 = 10). So the answer is "True". The pair [8,2] also satisfies the condition
Sample Input 1

3 5
-5 2 1

Sample Output 1

False

Explanation 1

None of the pairs [-5,2], [-5,1], [2,1] satisfy the given condition so the answer is "False"
'''

def sumPair(lst,s):
    c=0
    low=0
    high=len(lst)-1
    while(low<high):
        if(lst[low]+lst[high]==s):
            c+=1
            break
        if(lst[low]+lst[high]>s):
            high-=1
        else:
            low+=1
    return c

N,M=map(int,input().split())
nums=list(map(int,input().split()[:N]))
nums.sort()
c=sumPair(nums,M)
if(c>0):
    print(True)
else:
    print(False)