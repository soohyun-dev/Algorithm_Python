def check(depth):
    global sum, cnt

    if len(answer_check)==N:
        for i in range(N):
            sum=sum+answer_check[i]-K
            if sum < 500:
                break
        if sum>=500:
            cnt+=1
        sum=500  # sum 값 초기화
        return

    for i in range(N):
        if not visited[i]:
            visited[i]=True
            answer_check.append(A[i])
            check(depth+1)
            answer_check.pop()
            visited[i]=False

N,K=map(int,input().split())
A=sorted(list(map(int,input().split())))
visited=[False]*N
answer_check=[]
sum=500
cnt=0
check(0)
print(cnt)





