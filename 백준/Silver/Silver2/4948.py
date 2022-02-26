import sys
input=sys.stdin.readline

check=[False]*2+[True]*246911

for i in range(2,451):
    tmp=i+i
    for j in range(tmp,246913,i):
        check[j]=False

while True:
    n=int(input())
    if n==0:
        break
    cnt=0
    l=[]
    for i in range(n+1,(2*n)+1):
        if check[i]==True:
            cnt+=1
    print(cnt)




