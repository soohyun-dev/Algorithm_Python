import sys 
input=sys.stdin.readline

N,C=map(int,input().split())
wifi=[]
for i in range(N):
    wifi.append(int(input()))
wifi.sort()
close, far = 1, wifi[-1]
result=0

while close <= far:
    tmp=wifi[0]
    divide=(close+far)//2
    cnt=1
    for i in range(N):
        if wifi[i]>=tmp+divide:
            tmp=wifi[i]
            cnt+=1
    if cnt >= C:
        close=divide+1
        result=divide
    else:
        far=divide-1
    print(close, far, cnt)

print(result)




