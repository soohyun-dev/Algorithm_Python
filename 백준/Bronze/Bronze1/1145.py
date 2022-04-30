nums=list(map(int,input().split()))
N=min(nums)
while True :
    cnt=0
    for i in range(5):
        if N%nums[i]==0:
            cnt+=1
        
    if cnt>2:
        print(N)
        break
    N+=1