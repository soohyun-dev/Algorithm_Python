n,m,k=map(int,input().split())
matrix=[[0]*n for _ in range(m)]

for i in range(k):
    x1,y1,x2,y2,u=map(int,input().split())
    matrix[x1][y1]+=u
    matrix[x2+1][y2+1]+=u
    
    matrix[x1][y2+1]-=u
    matrix[x2+1][y1]-=u
    
    
for i in range(n):
    print(*matrix[i], end=' ')
    print()
    
for i in range(n):
    for j in range(1,m):
        matrix[i][j]+=matrix[i][j-1]
    
    if i!=n-1:
        matrix[i+1][0]+=matrix[i][-1]
print()
for i in range(n):
    print(*matrix[i], end=' ')
    print()