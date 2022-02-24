import sys
input=sys.stdin.readline

N,K=map(int,input().split())
country=[]
for _ in range(N):
    country.append(list(map(int,input().split())))

country.sort(key=lambda x:(-x[1],-x[2],-x[3]))
for i in range(N):
    if country[i][0]==K:
        cnt=i

for j in range(N):
    if country[cnt][1:]==country[j][1:]:
        print(j+1)
        break

