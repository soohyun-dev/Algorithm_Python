check=[]
for _ in range(10):
    check.append(list(map(int,input().split())))
result=[[0]*10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        if check[i][j]==-1:
            result[i][j]=-1
            
def right(result,a,b,cnt):
    for i in range(1,cnt+1):
        if b+i>9:
            break
        if result[a][b+i]==-1:
            break
        result[a][b+i]=-2
    return result

def left(result,a,b,cnt):
    for i in range(1,cnt+1):
        if b-i>9:
            break
        if result[a][b-i]==-1 or b-i<0:
            break
        result[a][b-i]=-2
    return result

def down(result,a,b,cnt):
    for i in range(1,cnt+1):
        if a+i>9:
            break
        if result[a+i][b]==-1 or a+i>9:
            break
        result[a+i][b]=-2
    return result

def up(result,a,b,cnt):
    for i in range(1,cnt+1):
        if a-i>9:
            break
        if result[a-i][b]==-1 or a-i<0:
            break
        result[a-i][b]=-2
    return result

for i in range(10):
    for j in range(10):
        tmp=check[i][j]
        if tmp!=0 and tmp!=-1:
            result[i][j]=-2
            if i==0: # 0행 
                if j==0:
                    result=right(result,i,j,tmp)
                    result=down(result,i,j,tmp)
                elif j==9:
                    result=left(result,i,j,tmp)
                    result=down(result,i,j,tmp)
                else:
                    result=left(result,i,j,tmp)
                    result=right(result,i,j,tmp)
                    result=down(result,i,j,tmp)
            elif i==9:
                if j==0:
                    result=right(result,i,j,tmp)
                    result=up(result,i,j,tmp)
                elif j==9:
                    result=left(result,i,j,tmp)
                    result=up(result,i,j,tmp)
                else:
                    result=left(result,i,j,tmp)
                    result=right(result,i,j,tmp)
                    result=up(result,i,j,tmp)
            else:
                if j==0:
                    result=right(result,i,j,tmp)
                    result=up(result,i,j,tmp)
                    result=down(result,i,j,tmp)
                elif j==9:
                    result=left(result,i,j,tmp)
                    result=up(result,i,j,tmp)
                    result=down(result,i,j,tmp)
                else:
                    result=left(result,i,j,tmp)
                    result=right(result,i,j,tmp)
                    result=up(result,i,j,tmp)
                    result=down(result,i,j,tmp)
    
N=int(input())
Player=[]
for i in range(1,N+1):
    x,y=map(int,input().split())
    x-=1
    y-=1
    if result[x][y]==-2:
        Player.append('dead')
    else:
        Player.append('survive')
        result[x][y]=i   
        
for i in range(10):
    print(*result[i],end=' ')
    print()
    
print('Character Information')
for i in range(N):
    if Player[i]=='dead':
        print('player %d dead' %(i+1))
    elif Player[i]=='survive':
        print('player %d survive' %(i+1))
    
    
    