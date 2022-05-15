import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
    l.append(list(map(int,input().split())))
    
l.sort(key=lambda x:(x[0]))
time=0
print(l)
for i in range(N):
    if l[i][0] >= time:
        time=(l[i][0]+l[i][1])
    else:
        time+=l[i][1]
    
print(time)

