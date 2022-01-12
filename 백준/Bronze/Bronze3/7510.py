cnt=int(input())
for i in range(1, cnt+1):
  A=sorted(map(int,input().split()))
  if(A[2]**2==(A[0]**2) + (A[1]**2)):
    print('Scenario #%d:' %(i))
    print('yes\n')
  else:
    print('Scenario #%d:' %(i))
    print('no\n')
   
