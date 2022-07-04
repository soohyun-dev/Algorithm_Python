n=int(input())
matrix=[[0]*n for _ in range(n)]

cnt=1
for i in range(n):
    for j in range(n):
        matrix[i][j]=cnt
        cnt+=1
        
for i in range(n):
    if i%2!=0:
        matrix[i].reverse()
  
for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()