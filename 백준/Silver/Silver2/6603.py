def dfs(depth):
    if len(answer_check)==6:
      if(str(answer_check) not in answer):
        print(' '.join(map(str, answer_check)))
        answer.append(str(answer_check))
        return
      else: 
        return

    for i in range(k):
      if depth==0 or (not visited[i] and (answer_check[depth-1] <= p[i])) :
        answer_check.append(p[i])
        visited[i]=True
        dfs(depth+1)
        visited[i]=False
        answer_check.pop()

while True:
  l=list(map(int, input().split()))
  if len(l)==1:
    break
  k=l[0]
  visited=[False]*k
  p=sorted(l[1:])
  answer=[]
  answer_check=[]
  dfs(0)
  print()
  