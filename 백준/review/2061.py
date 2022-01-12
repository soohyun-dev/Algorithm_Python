'''
1837 이랑 비교
L-1 해줄필요없고
BAD 출력하는 조건 바뀜
나머지는 비슷

'''

K,L=map(int,input().split())

a=[False, False] + [True] * (L)
prime=[]
for i in range(2, L+1):
  if a[i]:
    prime.append(i)
    for j in range(2*i, L+1, i):
      a[j]=False
result='GOOD'
for l in prime:
  if K%l==0 and l<L:
    result = f'BAD {l}'
    break
print(result) 




