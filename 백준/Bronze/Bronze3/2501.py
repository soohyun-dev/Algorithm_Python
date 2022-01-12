N,K = map(int,input().split())
aliquot=[0]  # K번째에 맞게 마지막에 출력하기 위해 빈배열이아닌 아무거나 하나 넣어줌.
sum=0
for i in range(1,N+1):
  if (N%i==0):
    aliquot.append(i)
    sum+=1  # 약수의 갯수
if sum<K:   # 약수의 갯수가 K보다 작을때
  print(0)
else:
  print(aliquot[K])

  



