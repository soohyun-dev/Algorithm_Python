n=int(input())
matrix=[[0]*n for _ in range(n)]

cnt=1
for i in range(n):
    for j in range(n):
        matrix[j][i]=cnt
        cnt+=1
        
for i in range(n):
    print(*matrix[i],end=' ')
    print()