N=int(input())
l=sorted(list(map(int,input().split())))
M=int(input())
T=list(map(int,input().split()))

def binary(x):
  left=0
  right=len(l)-1
  while left<=right:
    mid=(left+right)//2
    if l[mid] == x:
      return True
    elif l[mid]>x:
      right=mid-1
    elif l[mid]<x:
      left=mid+1


for i in range(len(T)):
  if binary(T[i])==True:
    print(1)
  else:
    print(0)


