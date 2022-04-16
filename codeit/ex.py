import sys
input=sys.stdin.readline

N=int(input())
nums=list(map(int,input().split()))
tmp=[]
visited=[False]*(N+1)
sum=0

def check(depth,idx):
    global sum

    if len(tmp)==2:
        sum+=tmp[0]*tmp[1]
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i]=True
            tmp.append(nums[i])
            check(depth+1, i+1)
            tmp.pop()
            visited[i]=False

check(0,0)
print(sum)

