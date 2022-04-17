N=int(input())
nums=list(map(int,input().split()))
hap=sum(nums)
sum=0
for num in nums:
    hap-=num
    sum+=num*hap
print(sum)

