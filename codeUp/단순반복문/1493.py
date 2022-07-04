n,m=map(int,input().split())
matrix=[]
result=[[0]*m for _ in range(n)]
for i in range(n):
    matrix.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(m):
        result[i][j]=sum(matrix[i][:j+1])
        if i>0:
            result[i][j]+=result[i-1][j]
            
for i in range(n):
    print(*result[i], end=' ')
    print()