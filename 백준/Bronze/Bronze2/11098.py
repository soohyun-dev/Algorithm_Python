for i in range(int(input())):
    MAX=0
    result=''
    for j in range(int(input())):
        p,n=input().split()
        if MAX<int(p):
            MAX=int(p)
            result=n
    print(result)
            