N,M=map(int,input().split())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))

M,K=map(int,input().split())
B=[]
for _ in range(M):
    B.append(list(map(int,input().split())))


s=[]
for i in range(N):
    tmp=[]
    for k in range(K):
        value=0
        for m in range(M):
            value+=(A[i][m]*B[m][k])
        tmp.append(value)
    s.append(tmp)

for i in range(N):
    print(*s[i])