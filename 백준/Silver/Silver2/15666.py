N,M=map(int,input().split())
l=sorted(list(map(int,input().split())))
answer_checked=[]
answer=[]

def check(depth):
  if len(answer_checked)==M:
    if str(answer_checked) not in answer:
      answer.append(str(answer_checked))
      print(' '.join(map(str, answer_checked)))
      return
    else:
      return
  
  for i in range(N):
    if depth==0 or answer_checked[depth-1]<=l[i]:
      answer_checked.append(l[i])
      check(depth+1)
      answer_checked.pop()

check(0)



