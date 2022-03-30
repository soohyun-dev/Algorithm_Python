def check(depth):
    if sum(answer_check)==S:
        if str(sorted(answer_check,reverse=True)) not in answer:
            answer.append(str(sorted(answer_check,reverse=True)))

    for i in range(N):
        if not visited[i]:
            visited[i]=True
            answer_check.append(A[i])
            check(depth+1)
            answer_check.pop()
            visited[i]=False


N,S=map(int,input().split())
A=list(map(int,input().split()))
visited=[False]*N
answer_check=[]
answer=[]
check(0)
cnt=len(answer)
if S==0:
    print(cnt-1)
else:
    print(cnt)

    