def track(A,B,C,P):
  return int(A*(B-P)**C)
def field(A,B,C,P):
  return int(A*(P-B)**C)
for i in range(int(input())):
  l=list(map(int,input().split()))
  sum=track(9.23076,26.7,1.835,l[0])+field(1.84523,75,1.348,l[1])+\
  field(56.0211,1.5,1.05,l[2])+track(4.99087,42.5,1.81,l[3])+\
  field(0.188807,210,1.41,l[4])+field(15.9803,3.8,1.04,l[5])+\
  track(0.11193,254,1.88,l[6])
  print(sum)
