N=int(input())
maze=list(map(int,input().split()))
if N==1:
    print(0)
else:
    check=[[0,0] for _ in range(N)]
    for i in range(N):
        for j in range(1,maze[i]+1):
            if i+j<N:
                if check[i+j][1]==0:
                    check[i+j][0]=check[i][0]+1
                    check[i+j][1]=1
                else:
                    check[i+j][0]=min(check[i][0]+1,check[i+j][0])
        if i+1<N:
            if check[i+1][0]==0:
                break
    if check[-1][0]==0:
        print(-1)
    else:
        print(check[-1][0]-1)