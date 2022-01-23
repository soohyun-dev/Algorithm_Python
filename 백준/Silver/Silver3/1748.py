N=int(input())
sum=0
cnt=9
num=1
if N < 10: # 10 미만의 숫자는 그대로 출력
  print(N)
else:
  while True:  # 자리수대로 끊어서 반복
    sum+=(cnt*num) 
    N-=cnt 
    cnt*=10  # 자릿수에 해당되는 갯수
    num+=1  # 자릿수
    if cnt>N:  # 더이상 자리수를 늘리지 않아도 될 때
      sum+=(num*N)
      break
  print(sum)

