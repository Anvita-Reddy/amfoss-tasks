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
