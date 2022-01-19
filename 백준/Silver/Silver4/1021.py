from collections import deque

N,M=map(int,input().split())
l=(list(map(int, input().split())))
dq=deque((list(i for i in range(1,N+1))))

cnt=0

while len(l)!=0:
  if dq[0]==l[0]: # 첫번째 연산 수행
    del(dq[0])
    del(l[0])
  else:
    if dq.index(l[0])>len(dq)//2:  # 세번째 연산 수행
      a=dq.pop()
      dq.appendleft(a)
      cnt+=1
    else:  # 두번째 연산 수행
      b=dq.popleft()
      dq.append(b)
      cnt+=1

print(cnt)

