a,b=map(int,input().split())
score=[]
if a%2==0:
    tmp=a//2
else:
    tmp=a//2+1
for i in range(tmp,a+1):
        score.append([i,a-i])
for i in range(len(score)):
    if score[i][0]-score[i][1]==b:
        print(score[i][0],score[i][1])
        check=True
        exit(0)
print(-1)