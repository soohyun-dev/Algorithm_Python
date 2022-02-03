import sys
input=sys.stdin.readline

Eratosth=[False]*2+[True]*9999


for i in range(2,8):  # 에러노트테네스의 체
  tmp=i+i
  for j in range(tmp,10001,i):
    Eratosth[j]=False

for i in range(int(input())):
  num=int(input())
  divide=num//2
  for j in range(divide,0,-1):
    if Eratosth[j]==True:
      if Eratosth[num-j]==True:
        print(j, num-j)
        break