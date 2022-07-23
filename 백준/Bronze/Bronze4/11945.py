N,M=map(int,input().split())
check=[]
for i in range(N):
    check.append(input())
    
for i in range(N):
    print(check[i][::-1])