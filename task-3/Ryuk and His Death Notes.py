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
