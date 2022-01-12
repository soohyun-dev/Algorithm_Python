n=int(input())
a=2
cnt=0  # 2로 몇번 빼줘야 하는지 세주는 역할
s=n-(a*cnt)
if s%5==0:  # 5로 바로 나누어 떨어질 때
  print(n//5)
else:  # 2로 빼줘야 할때
  while s%5!=0:
    s=n-(a*cnt)  # while 문 내에서 s가 정의 되기 위해서 재정의
    if s%5==0:
      print((s//5)+cnt)
    else:
      cnt+=1
    if s<0:  # 2를 아무리 빼도 2나 5로 나누어지는 순간이 없을 때
      print(-1)
      break


