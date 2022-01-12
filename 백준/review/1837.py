P,K=map(int,input().split())

# K보다 작은 소수들 구하기 (에라토스테네스의 체)
K -= 1   #소수는 K보다 작기때문에
a=[False, False] + [True] * (K-1)
prime=[]
for i in range(2, K+1):
  if a[i]:
    prime.append(i)
    for j in range(2*i, K+1, i):  # 범위내 소수의 배수들 제거
      a[j]=False
result='GOOD'
for k in prime:
  if P % k ==0:
    result = f'BAD {k}'
    break
print(result)

