a,b=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
cnt=0
same=0
check={}

for i in A:
    check[i]=True

for i in B:
    if check.get(i)==True:
        same+=1
    else:
        cnt+=1

print(cnt + (a-same))
    

