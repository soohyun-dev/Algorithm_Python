N=int(input())
cnt=[0]*1000001
sum=0

for i in list(map(int,input().split())):
    cnt[i]+=1

for i in list(map(int,input().split())):
    if cnt[i]>=1:
        cnt[i]-=1
    else:
        sum+=1
        
print(sum)
