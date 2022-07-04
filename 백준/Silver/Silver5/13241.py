A,B=map(int,input().split())
if A==B:
    print(A)
else:
    check=False
    result=A*B
    tmp=A
    while True:
        tmp+=A
        if tmp%B==0:
            check=True
            break
        if tmp==result:
            break

    if check==False:
        print(result)
    else:
        print(tmp)
        
        
        
        