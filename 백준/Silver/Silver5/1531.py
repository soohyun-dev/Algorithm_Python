N,M=map(int,input().split())
paper=[[0]*100 for _ in range(100)]

for i in range(N):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            paper[i][j]+=1
            
cnt=0
for i in range(100):
    for j in range(100):
        if paper[i][j]>M:
            cnt+=1
            
print(cnt)
                