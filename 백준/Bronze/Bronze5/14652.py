N,M,K = map(int,input().split())
A=K//M
B=K%M
print(A,B)


'''
메모리초과
d=[[0]*N for a in range(M)]
sum=0
for i in range(N):
    for j in range(M):
        d[i-1][j-1]=sum
        sum+=1
        if(d[i-1][j-1]==K):
            print(i,j)
'''
