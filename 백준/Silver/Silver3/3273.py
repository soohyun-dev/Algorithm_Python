import sys
input=sys.stdin.readline

n=input()
check=[0]*2000001
i=1
l=[]
for n in map(int,input().split()):
    check[n]=i
    i+=1
    l.append(n)
num=int(input())

cnt=0
for n in l:
    if check[n] < check[num-n]:
        cnt+=1
print(cnt)

