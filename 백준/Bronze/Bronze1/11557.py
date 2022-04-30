import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    m=0
    name='a'
    for i in range(N):
        university, cnt = input().split()

        if int(cnt)>m:
            m=int(cnt)
            name=str(university)

    print(name)