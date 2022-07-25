
import random
N=int(input())
num=[ i for i in range(1,24)]
LIST=[]
for i in range(N):
    LIST.append(*random.sample(num,1))
    
print(*LIST)