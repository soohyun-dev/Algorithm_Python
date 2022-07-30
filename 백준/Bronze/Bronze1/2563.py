paper=[[[0] for _ in range(100)] for _ in range(100)]

for _ in range(int(input())):
    a,b=map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            paper[i][j]=1

result=0
for i in range(100):
    for j in range(100):
        if paper[i][j]==1:
            result+=1
            
print(result)