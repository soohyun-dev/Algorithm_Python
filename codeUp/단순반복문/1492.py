from re import L


n=int(input())
nums=list(map(int,input().split()))

for i in range(n):
    print(sum(nums[:i+1]), end=' ')