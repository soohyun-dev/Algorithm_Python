import sys
input=sys.stdin.readline

def gcd(x,y):
    if y==0:
        return x
    tmp = x%y
    return gcd(y, tmp)

N=int(input())
for _ in range(N):
    l=sorted(list(map(int,input().split())))
    g=[1]
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            g.append(gcd(l[i],l[j]))
    print(max(g))