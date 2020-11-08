'''
Ryuk and His Death Notes

Ryuk after giving his Death Note to Light Yagami got a wonderful idea,
that he should be making Death Notes out of all the papers he has and then distributing them all to the Foss members.
There are different types of papers in a death note. 
For example to make a particular kind of death note needs to 2 Types of pages i.e 3 red pages and 2 yellow pages might be required.
So in order to make that particular death note Ryuk must be having 3 red pages and 2 yellow pages,
even if a single page is missing in either type of the pages he can’t make the death note. Ryuk wants you to find out the number of death notes he can make.

Input Format

First line contains N, the number of different types of papers he need to create a Single Death Note.

The next line consists of N space separated numbers (a1 to an) stating the requirement of each type of paper to create the Death Note.

The next line consists of N space separated numbers (b1 to bn) representing the number of pages of each type of paper which are available to Ryuk.

Constraints

1<=N<=10^6

1<=a1,a2….an<=10^9

1<=b1,b2….bn<=10^9

Output Format

Print the number of Death Notes Ryuk could create.

Sample Input 0

4
10 2 13 20
11 100 130 97

Sample Output 0

1

Explanation 0

Here we have 4 types of pages to create a Single Death Note.
We need 10 pages of Type-1 and 2 pages of Type-2 and 13 pages of Type-3 and 20 pages of Type-4 to create a Single Death Note.
There are 11 pages of Type-1, 100 pages of Type-2,130 pages of Type-3 and 97 pages of Type-4.
So he can create 1 Death Notes at Maximum because pages of Type-1 will not be sufficient for 2nd Death Note.
So he cant create anymore DeathNote further

'''

N=int(input())
req=list(map(int,input().split()[:N]))
ava=list(map(int,input().split()[:N]))
note=0
while(True):
    res=0
    for i in range(N):
        if(ava[i]>=req[i]):
            res+=req[i]
            ava[i]-=req[i]
    if(res==sum(req)):
        note+=1
    else:
        break
print(note)
