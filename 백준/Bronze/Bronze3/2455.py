tmp=0
sum=0
for i in range(4):
    a, b = map(int,input().split())
    sum+=b
    sum-=a
    if tmp < sum:
        tmp=sum
print(tmp)