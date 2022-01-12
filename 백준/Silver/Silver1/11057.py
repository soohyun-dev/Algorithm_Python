n = int(input())

num = [1]*10

for i in range(n-1):
    for j in range(1, 10):
        num[j] += num[j-1]
        
print(sum(num)%10007)


'''
N=int(input())
x=1
num=str(x).zfill(N)
cnt=0
if N==1:
  print(10)
else:
  while len(num)==N:
    num=str(x).zfill(N)
    num=list(num)
    a=0
    for i in range(len(num)-1):
      if int(num[i])<int(num[i+1]):
        a=1
      elif int(num[i])>int(num[i+1]):
        a=0
        break
    if a==1:
      cnt+=1
    x=int(x)+1
  print((cnt+10)%10007)
'''
