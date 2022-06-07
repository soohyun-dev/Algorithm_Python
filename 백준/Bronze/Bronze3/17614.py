N=int(input())
sum=0

for i in range(1,N+1):
   sum+= str(i).count('3')+str(i).count('6')+str(i).count('9')
            
print(sum)