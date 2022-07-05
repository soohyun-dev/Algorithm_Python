check=[]
for _ in range(25):
    check.append(list(map(int,input().split())))
    
new=[[0]*25 for _ in range(25)]
for i in range(1,24):
    for j in range(1,24):
        tmp=[check[i-1][j-1],check[i-1][j],check[i-1][j+1],check[i][j-1],check[i][j+1],check[i+1][j-1],check[i+1][j],check[i+1][j+1]]
        cnt=tmp.count(1)
        if check[i][j]==0 and cnt==3:
            new[i][j]=1
        elif check[i][j]==1 and (cnt>=4 or cnt<=1):
            new[i][j]=0
        elif check[i][j]==1 and (cnt==2 or cnt==3):
            new[i][j]=1

for i in range(25):
    print(*new[i], end=' ')
    print()