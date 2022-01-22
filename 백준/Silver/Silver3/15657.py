N,M = map(int,input().split())
l=sorted(list(map(int,input().split())))
answer=[]

def check(depth) :
  if len(answer)==M:
    print(' '.join(map(str, answer)))
    return

  for i in range(N):
    if depth==0 or answer[depth-1] <= l[i]:  # 초기값 0을 넣었을 때를 위해 앞에 depth==0 조건
      answer.append(l[i])
      check(depth+1)
      answer.pop()

check(0)


