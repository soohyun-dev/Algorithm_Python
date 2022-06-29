N=int(input())
cnt=1
sum=0
for i in range(N):
    sum+=(cnt*(N-i))
    cnt+=1
print(sum)