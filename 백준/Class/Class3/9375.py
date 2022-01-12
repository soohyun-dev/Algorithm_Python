from collections import Counter

for _ in range(int(input())):
  N=int(input())
  l=[]
  for i in range(N):
    front, back = input().split()
    l.append(back)  # 종류만 알면 됨.
  check = Counter(l)  # 각 종류의 갯수 체크
  result=1
  if len(check)==1:    # 한가지의 종류만 있을 때
    print(check[back])
  else:
    for i in check:
      result*=check[i]+1
    print(result-1)  # 1을 빼주는 이유는 하나도 안입었을때 제외해주기
  
   
 

