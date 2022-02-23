import sys
input=sys.stdin.readline

N,K=map(int,input().split())
country=[]
for _ in range(N):
    country.append(list(map(int,input().split())))

country.sort(key=lambda x:(-x[1],-x[2],-x[3]))
cnt=1
if country[0][0]==K:
        print(cnt)
else:
    for i in range(1,N):
        if country[i][0]==K:
            print(cnt)
            break
        if country[i-1][1:]!=country[i][1:]:
            cnt+=1


