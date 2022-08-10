for _ in range(int(input())):
    N,M=map(int,input().split())
    if M<4 or N<12:
        print(-1)
    else:
        print(11*M+4)