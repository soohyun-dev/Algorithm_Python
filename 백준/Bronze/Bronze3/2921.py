N=int(input())
up=[]
down=[]
for i in range(1,N+1):
    down.append(i)
    for j in range(1,i+1):
        down.append(i)
        up.append(j)
print(sum(up)+sum(down))
        
        
        