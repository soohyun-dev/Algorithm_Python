for _ in range(int(input())):
    N,D,A,B,F=map(float,input().split())
    value=D/(A+B)
    print(int(N), format(value*F, ".6f"))