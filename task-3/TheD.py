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