import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    cnt=1
    sum=0
    while True:
        if N-cnt-(cnt*cnt) >= 0:
            cnt+=1
        else:
            cnt-=1
            break
    print(cnt)