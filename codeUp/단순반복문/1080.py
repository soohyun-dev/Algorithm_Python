N=int(input())
cnt=1
sum=0
while True:
    sum+=cnt
    if sum>=N:
        print(cnt)
        break
    cnt+=1