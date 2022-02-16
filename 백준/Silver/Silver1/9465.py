import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    up=list(map(int,input().split()))
    down=list(map(int,input().split()))
  
    if n>1:
        up[1]+=down[0]
        down[1]+=up[0]
        for i in range(2,n):
            up[i]+=max(down[i-1], down[i-2])
            down[i]+=max(up[i-1], up[i-2])
        print(up,down)
    print(up[-1],down[-1])