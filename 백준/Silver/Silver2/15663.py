N,M=map(int,input().split())
l=sorted(list(map(int,input().split())))
answer_check=[]
answer=[]
visited=[False]*N

def check(depth):
  if len(answer_check)==M:
    if str(answer_check) not in answer:
      print(' '.join(map(str,answer_check)))
      answer.append(str(answer_check))
      return
    else:
      return
  for i in range(N):
    if not visited[i]:
      visited[i]=True
      answer_check.append(l[i])
      check(depth+1)
      visited[i]=False
      answer_check.pop()

check(0)


