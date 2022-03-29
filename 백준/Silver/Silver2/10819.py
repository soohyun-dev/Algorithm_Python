def check(depth):
    if len(M)==N:
        global total
        sum=0
        for i in range(N-1):
            sum+=abs(M[i]-M[i+1])
        total=max(sum,total)
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            M.append(l[i])
            check(depth+1)
            M.pop()
            visited[i]=False

N=int(input())
l=list(map(int,input().split()))
visited=[False]*N
M=[]
total=0

check(0)

print(total)

