N,M=map(int,input().split())
l=sorted(list(map(int,input().split())))
answer=[]

def check(depth):
  if depth==M:
    print(' '.join(map(str,answer)))
    return
    
  for i in range(N):
    if depth==0 or answer[depth-1] < l[i]: # depth==0 이 뒤로 오면 인덱스 오류 , 오름차순 정리
      answer.append(l[i])
      check(depth+1)     
      answer.pop()      

check(0)


