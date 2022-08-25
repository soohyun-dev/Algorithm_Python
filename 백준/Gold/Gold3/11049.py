import sys
input=sys.stdin.readline
              
def DP(matrix):              
    dp=[[ 0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N-i):
            x=i+j
            if j!=x:
                dp[j][x]=sys.maxsize
                for k in range(j,x):
                    dp[j][x]=min(dp[j][x],dp[j][k]+dp[k+1][x]+matrix[j]*matrix[k+1]*matrix[x+1])
    for i in range(N):
        print(dp[i])
    return dp[0][-1]

N=int(input())
matrix=[]
for i in range(N):
    a,b=map(int,input().split())
    matrix.append(a)
    if i==N-1:
        matrix.append(b)
        
print(DP(matrix))


