check=[0]*24
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    check[l[i]]+=1
print(*check[1:])