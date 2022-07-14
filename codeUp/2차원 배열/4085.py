m,n,x,y=map(int,input().split())
place=[]
for _ in range(n):
    place.append(list(map(int,input().split())))

result=0
for i in range(n-y+1):
    for j in range(m-x+1):
        tmp=0
        for k in range(y):  
            tmp+=sum(place[i+k][j:j+x])
        if tmp>result:
            result=tmp
print(result)
            
            