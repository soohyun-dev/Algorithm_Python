N,M=map(int,input().split())
l=sorted(list(map(int,input().split())))
answer_checked=[]
answer={}

def check(depth):
  if depth==M:
    a= ' '.join(map(str, answer_checked))
    if a not in answer:
      print(a)
      answer[a]=True
    return ;
  for i in range(N):
      answer_checked.append(l[i])
      check(depth+1)
      answer_checked.pop()
  
check(0)


