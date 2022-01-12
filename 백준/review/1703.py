import sys

count=int(sys.stdin.readline())
sum=1
for i in range(count):
  cntNum = int(sys.stdin.readline())
  sum+=cntNum
print(sum-count)




'''
시간 초과

count = int(input())
sum=1
for i in range (count):
  num=int(input())
  sum+=num
print(sum-(count))



A=[]
sum=0
for i in range(count):
  num=int(input())
  A.append(num)
for j in range(count-1):
  sum+=int(A[j])-1
print(sum+int(A[count-1]))
'''