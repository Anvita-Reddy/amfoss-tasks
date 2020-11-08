''' 
Infinity Stones

In a parallel universe there are N infinity stones (not just 6 ;) ).
The infinity stones can only exist inside boxes. There are M boxes in the universe.
It is guaranteed that no infinity stones are outside the M boxes. Thanos is on the search for the infinity stones.
The avengers can protect atmost K boxes. So they want to find out if is possible to transfer all infinity stones to atmost K boxes.
A box i has a maximum capacity S[i] i.e it cannot store more than S[i] infinity stones. A box i initially has some A[i] infinity stones.
Find out if the avengers can protect all the stones(Note that the avengers can guard atmost K boxes).
Output YES if it is possible to do so and NO if it is not possible.

Input Format

The first line contains the number of test cases, t.

The first line of every test case contains three space separated integers N, M and K representing the number of infinity stones,
the number of boxes and the maximum number of boxes the avengers can protect respectively.

The second line of every test case contains M space separated integers where the i th integer represents the number of stones in the i th box.

The third line contains M space separated integers where the i th integer represents the maximum capacity of the i th box.

Constraints

1 < t < 20

1 <= M <= 10000

0 <= A[i] <= S[i] < 100000

Output Format

Output "YES" if transfer is possible and "NO" if it is not possible to do so.

Sample Input 0

3
10 6 3
3 3 1 1 1 1
4 4 8 2 3 4
10 3 5
6 3 1
7 3 2
10 2 1
5 5
5 6

Sample Output 0

YES
YES
NO

Explanation 0

For the first test case it's possible to move stones from boxes 3,4,5 to box 2.
Final configuration would be 3 3 4 0 0 0 and it would not violate the max capacity of the boxes.
As the avengers can protect atmost 3 boxes this configuration is valid

For the second test case the avengers can protect atmost 5 boxes. As there are only 3 boxes they can protect all of them

For the third test case the avengers can protect atmost 1 box and it's not possible to transfer all stones to 1 box (due to max capacity reasons)

'''

def infinityStones():
    n,m,k=map(int,input().split())
    ava=list(map(int,input().split()[:m]))
    cap=list(map(int,input().split()[:m]))
    if(k>m):
        return 'YES'
    else:
        cap.sort(reverse=True)
        max_cap=0
        for i in range(k):
            max_cap+=cap[i]
        if(sum(ava)<=max_cap):
            return 'YES'
        else:
            return 'NO'
t=int(input())
x=[]
for i in range(t):
    x.append(infinityStones())
for i in x:
    print(i)
