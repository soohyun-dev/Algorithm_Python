import sys
input=sys.stdin.readline

cnt=0
while True:
    L,P,V=map(int,input().split())
    if L==0 and P==0 and V==0:
        break

    value=V//P
    day=value*L

    rest=V%P
    if rest>=L:
        day+=L
    else:
        day+=rest
    cnt+=1
    print('Case %d: %d' %(cnt, day))
    
    