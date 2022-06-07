N=int(input())
milk=list(map(int,input().split()))
milk.append(3)
cnt=0

for i in range(N):
    if milk[i]==cnt%3:
        cnt+=1
print(cnt)
