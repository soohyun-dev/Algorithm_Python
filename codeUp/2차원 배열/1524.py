check=[]
for x in range(9):
    check.append(list(map(int,input().split())))
x,y=map(int,input().split())
x-=1
y-=1
if check[x][y]==1:
    print(-1)
else:
    if x==0:
        if y==0:
            tmp=[check[x][y+1],check[x+1][y],check[x+1][y+1]]
        elif y==8:
            tmp=[check[x][y-1],check[x+1][y-1],check[x+1][y]]
        else:
            tmp=[check[x][y-1],check[x][y+1],check[x+1][y-1],check[x+1][y],check[x+1][y+1]]
                
    elif x==8:
        if y==0:
            tmp=[check[x][y+1],check[x-1][y],check[x-1][y+1]]
        elif y==8:
            tmp=[check[x][y-1],check[x-1][y-1],check[x-1][y]]
        else:
            tmp=[check[x][y-1],check[x][y+1],check[x-1][y-1],check[x-1][y],check[x-1][y+1]] 
    else:
        if y==0:
            tmp=[check[x-1][y],check[x-1][y+1],check[x][y+1],check[x+1][y],check[x+1][y+1]]
        elif y==8:
            tmp=[check[x-1][y-1],check[x-1][y],check[x][y-1],check[x+1][y-1],check[x+1][y]]
        else:
            tmp=[check[x-1][y-1],check[x-1][y],check[x-1][y+1],check[x][y-1],check[x][y+1],check[x+1][y-1],check[x+1][y],check[x+1][y+1]]
            
    print(tmp.count(1))