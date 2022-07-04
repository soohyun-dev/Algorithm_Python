n,m=map(int,input().split())
check=[[0]*m for _ in range(n)]
cnt=0
x=0
y=m-1
Y=0
X=n
tmp=0
while True:
    while x<X-1:
        if cnt>=(n*m):
            break
        else:
            cnt+=1
        check[x][y]=cnt
        x+=1
    while y>Y:
        if cnt>=(n*m):
            break
        else:
            cnt+=1
        check[x][y]=cnt
        y-=1
    X=y
    Y=x
    while x>X:
        if cnt>=(n*m):
            break
        else:
            cnt+=1
        check[x][y]=cnt
        x-=1
    while y<Y-1:
        if cnt>=(n*m):
            break
        else:
            cnt+=1
        check[x][y]=cnt
        y+=1
    for i in range(n):
        print(*check[i],end=' ')
        print()
    X=n-x-1
    Y=x+1
    if tmp==20:
        break
    if X==Y and X-x==1:
        check[x][y]=cnt+1
        break
    if cnt>=(n*m):
            break
        
        
for i in range(n):
    print(*check[i],end=' ')
    print()
