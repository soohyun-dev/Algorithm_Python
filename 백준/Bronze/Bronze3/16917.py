A,B,C,X,Y=map(int,input().split())

if A+B < C*2:
    print(A*X + B*Y)
else:
    print(2*C*min(X,Y) + min(A, C*2)*max(0,X-Y) + min(B,C*2)*max(0, Y-X))

