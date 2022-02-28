matrix=[[1]*201 for _ in range(201)]

for i in range(1,201):
    matrix[1][i]=i

for i in range(2,201):
    for j in range(2,201):
        matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]

N,M=map(int,input().split())
print(matrix[N][M]%1000000000)
