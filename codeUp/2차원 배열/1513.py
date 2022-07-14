N=int(input())
check=[[0]*N for _ in range(N)]
cnt=1
y=0
for i in range(N):
    if i==N-1:
        check[N-1][N-1]=cnt
        break
    elif i%2==0 and i>0:
        y+=1
    if i%2==0:  
        for j in range(N-1,i-1,-1):
            check[j][y]=cnt
            if j!=i:
              y+=1
            cnt+=1
    if i%2!=0:
        for j in range(i,N):
            check[j][y]=cnt
            if j!=N-1:
                y-=1
            cnt+=1
            
for i in range(N):
    print(*check[i], end=' ')
    print()
    
    