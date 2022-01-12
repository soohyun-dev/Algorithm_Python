M=int(input())
M=1000-M
sum=0
c=[500,100,50,10,5,1]
for i in range(6):  
  cnt=M//c[i]
  sum+=cnt
  M=M-c[i]*cnt

print(sum)


