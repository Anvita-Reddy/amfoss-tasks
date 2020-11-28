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