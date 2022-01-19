N,M = map(int,input().split())
l=sorted(list(map(int,input().split())))
answer=[]  # 출력시킬 리스트
visited=[False]*N  # 방문 확인

def check(depth):  # 함수(숫자) 구조이다. 

  if depth==M:  # 숫자가 주어진 M 값과 같을 경우 출력한다. 
    print(' '.join(map(str, answer)))
    return

  for i in range(N):
    if not visited[i]:  # 중복을 방지한다.
      visited[i]=True  # 방문 표시 해주고
      answer.append(l[i])  # 그 값을 리스트에 보관해둔다.

      # 함수 재호출, 그리고 다음 값을 돌려 이값이 주어진 M과 같은지 아니면 리스트에 더 저장할지를 판단한다.
      check(depth+1)  

      visited[i]=False 
      answer.pop()  # 끝 값만 제거해 순차적으로 호출

check(0)