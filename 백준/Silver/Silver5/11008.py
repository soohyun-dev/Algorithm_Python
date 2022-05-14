import sys
input=sys.stdin.readline

for i in range((int(input()))):
    s,p = input().split()
    s=s.replace(p, '0')

    print(len(s))

    