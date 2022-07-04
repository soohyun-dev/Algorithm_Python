N=int(input())

check=[[0]*N for _ in range(N)]
cnt=1
sum=0
for i in range(N):
    for j in range(N):
        if i==0 or i==N-1:
            sum+=cnt
        else:
            if j==0 or j==N-1:
                sum+=cnt
        check[i][j]=cnt
        cnt+=1
print(sum)