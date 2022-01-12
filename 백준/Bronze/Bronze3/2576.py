A=[]
sum=0   # 홀수 갯수 저장
s=0     # 홀수 합 저장
for i in range(7):
  num=int(input())
  if(num%2!=0):
    A.append(num)  # 홀수 A에 넣어주기
    sum+=1         # 홀수 갯수
if (sum!=0):
  for j in range(sum):
    s+=A[j]
  print(s)
  print(min(A))
else:       # 홀수가 없었을경우
  print(-1)

