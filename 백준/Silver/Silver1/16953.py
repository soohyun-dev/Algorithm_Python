A,B=map(int,input().split())
cnt=0
a=0
while True:
  if B==A:  # A와 B 가 같은 경우
    break
  elif B<A:  # B가 A보다 작아지는 경우, 연산 불가
    a=1
    break

  if B%2==0:  # B 가 2로 나누어 질 때
    B=int(B/2)
    cnt+=1
  else:      # B가 2로 나누어지지 않고 1을 빼줘야 할때
    B=str(B)
    if B[-1]=='1':  
      B=B[:-1]
      B=int(B)
      cnt+=1
    else:  # 만약 2로 나누어지지 않는데, 뒷자리가 1도 아니다? 바로 틀림
      a=1
      break 

if a==0:
  print(cnt+1)
else:
  print(-1)

  