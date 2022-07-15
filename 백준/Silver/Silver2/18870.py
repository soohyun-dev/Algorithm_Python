N=int(input())
nums=list(map(int,input().split()))
zip=sorted(list(set(nums)))

check={}
cnt=0
for i in zip:
    check[i]=cnt
    cnt+=1
    
for i in nums:
    print(check[i], end=' ')
    
    