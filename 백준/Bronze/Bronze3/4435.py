cnt=1
for _ in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=[1,2,3,3,4,10]
    y=[1,2,2,2,3,5,10]
    A=0
    B=0
    for i in range(6):
        A+=a[i]*x[i]
    for j in range(7):
        B+=b[j]*y[j]
    if A>B:
        print('Battle %d: Good triumphs over Evil' %(cnt))
    elif A<B:
        print('Battle %d: Evil eradicates all trace of Good' %(cnt))
    elif A==B:
        print('Battle %d: No victor on this battle field' %(cnt))
    cnt+=1