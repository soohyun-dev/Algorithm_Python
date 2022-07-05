a,b=map(int,input().split())
x,y,z=map(int,input().split())
check=[]
for _ in range(a):
    check.append(list(map(int,input().split())))
    
new=[[0]*b for _ in range(a)]
k=int(input())
for _ in range(k):
    for i in range(a):
        for j in range(b):
            if i==0:
                if j==0:
                    tmp=[check[i][j+1],check[i+1][j],check[i+1][j+1]]
                elif j==b-1:
                    tmp=[check[i][j-1],check[i+1][j-1],check[i+1][j]]
                else:
                    tmp=[check[i][j-1],check[i][j+1],check[i+1][j-1],check[i+1][j],check[i+1][j+1]]
            elif i==a-1:
                if j==0:
                    tmp=[check[i][j+1],check[i-1][j],check[i-1][j+1]]
                elif j==b-1:
                    tmp=[check[i][j-1],check[i-1][j-1],check[i-1][j]]
                else:
                    tmp=[check[i][j-1],check[i][j+1],check[i-1][j-1],check[i-1][j],check[i-1][j+1]] 
            else:
                if j==0:
                    tmp=[check[i-1][j],check[i-1][j+1],check[i][j+1],check[i+1][j],check[i+1][j+1]]
                elif j==b-1:
                    tmp=[check[i-1][j-1],check[i-1][j],check[i][j-1],check[i+1][j-1],check[i+1][j]]
                else:
                    tmp=[check[i-1][j-1],check[i-1][j],check[i-1][j+1],check[i][j-1],check[i][j+1],check[i+1][j-1],check[i+1][j],check[i+1][j+1]]
            
            cnt=tmp.count(1)
            if check[i][j]==0 and cnt==x:
                new[i][j]=1
            elif check[i][j]==1 and (cnt<y or cnt>=z):
                new[i][j]=0
            else:
                new[i][j]=check[i][j]

for i in range(a):
    print(*new[i], end=' ')
    print()