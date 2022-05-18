import sys
input=sys.stdin.readline

a=1
b=1

l=[0, 1,1]
for i in range(38):
    tmp=b
    b+=a
    a=tmp
    l.append(b)
    
N=int(input())
for _ in range(N):
    num=int(input())
    if num==0:
        print(1, 0)
    else:
        print(l[num-1], l[num])
    
    