check=[[] for _ in range(10)]
for i in range(10):
    check[i]=(list(map(int,input().split())))
place=list(map(int,input().split()))

for j in range(10):
    boo=True
    if place[j]==1:
        for k in range(9,-1,-1):            
            if check[k][j]>0:
                boo=False
                print('%d crash' %(j+1))
                break
            elif check[k][j]<0:
                boo=False
                print('%d fall' %(j+1))
                break
        if boo==True:
                print('%d safe' %(j+1))
    