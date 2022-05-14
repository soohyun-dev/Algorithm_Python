import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
    l.append(list(map(int,input().split())))

l.sort(key=lambda x:(x[0],x[1]))
check=[True]*N
cnt=0
for i in range(N):
    for j in range(i+1,N):
        if check[i]==False:
            break
        if l[i][0] <= l[j][0]:
            if l[i][1] <= l[j][1]:
                if check[j]==True:
                    check[j]=False
                    cnt+=1

print(N-cnt)

