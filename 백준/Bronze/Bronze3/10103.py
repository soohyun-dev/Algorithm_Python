A=B=100
N=int(input())
for i in range(N):
  a, b = map(int, input().split())
  if a > b:
    B-=a
  elif a < b:
    A-=b 
print(A, B ,sep='\n')



