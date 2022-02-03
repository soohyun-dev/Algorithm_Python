def dfs(depth):
  if len(answer)==N:
    print(' '.join(map(str, answer)))
    return
  
  for i in range(N):
    if not visited[i]:
      answer.append(l[i])
      visited[i]=True
      dfs(depth+1)
      visited[i]=False
      answer.pop()

N=int(input())
l=[]
answer=[]
visited=[False]*N
for i in range(1,N+1):
  l.append(i)

dfs(0)



