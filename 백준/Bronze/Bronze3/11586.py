import sys
input=sys.stdin.readline

N=int(input())
mirror=[]
for _ in range(N):
    mirror.append(list(input().rstrip('\n')))
state=int(input())
if state==1:
    for i in range(N):
        print(''.join(mirror[i]))
elif state==2:
    for i in range(N):
        print(''.join(mirror[i])[::-1])
elif state==3:
    for i in range(N-1,-1,-1):
        print(''.join(mirror[i]))
        
        