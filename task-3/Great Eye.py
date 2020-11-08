'''
Great Eye
The Sharingan is one of the Three Great Eye Techniques. 
It is Used by members of the Uchiha clan. Sauske is one of the last few Uchiha's alive.
Unfortunately he still hasn't awakened his Mangekyō Sharingan yet. So his visual powers are limited.
Naruto decides to take this as an advantage and challenges him in a contest. Sauske can't refuse the contest.
But he also dosen't want to loose. So he asks you for help. Since it is not common for an Uchiha to ask for help you also can't refuse.
The contest is as follows

Naruto gives sauske a sentence and a number 'k'. The sentence contains a number of words which are seperated by space, the words are numbered from 0.
You are supposed to print the sum of the ascii values of all the characters in the k'th word of the sentence.
There is no gaurentee that there exists a k'th word in the sentence. If it does not exist simply print -1.

Input Format

The first line contains a number 't' denoting the number of test cases.

2*t lines follow

The first line of every test case contains k The second line contains the sentence.

Constraints

t <= 20

Each sentence will contain a maximum of 200 words

Each word will only be a combination of lower case and upper case letters. Special Characters of any format will not be there. Length of each word will not exceed 20.

1 <= k <= 300

Output Format

For each test case print the output in a new line

Sample Input 0

3
1
Hello World
2
All the best
3
Amrita University

Sample Output 0

520
430
-1
'''

def greatEye():
    k=int(input())
    sen=input().split()
    if(k<len(sen)):
        wrd=sen[k]
        res=0
        for i in range(len(wrd)):
            if(wrd[i].isalpha()):
                res+=ord(wrd[i])
        return res
    else:
        return -1
t=int(input())
n=[]
for i in range(t):
    n.append(greatEye())
for i in n:
    print(i)
