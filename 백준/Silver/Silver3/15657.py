N,M = map(int,input().split())
l=sorted(list(map(int,input().split())))
visited=[False]*N
answer=[]
def check(depth) :
  if len(answer)==M:
    print(' '.join(map(str, answer)))
    return

  for i in range(N):
    if depth==0 or answer[depth-1] <= l[i]:
      answer.append(l[i])
      check(depth+1)
      answer.pop()

check(0)