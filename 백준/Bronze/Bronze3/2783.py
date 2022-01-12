X,Y=map(int,input().split())
cnt=1000/Y
sum=X*cnt
for i in range(int(input())):
  a,b=map(int,input().split())
  cnt_n=1000/b
  sum_n=a*cnt_n
  if(sum>sum_n):   # 만약 다른지점이 더 싸다면 그 값을 저장해둠.
   sum=sum_n
print(sum)

