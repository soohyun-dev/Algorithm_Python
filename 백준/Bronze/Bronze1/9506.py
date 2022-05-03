while True:
    N=int(input())
    if N==-1:
        break
    divisor=[1]
    tmp=N//2
    
    for i in range(2,tmp+1):
        if N%i==0:
            divisor.append(i)
    
    if sum(divisor)==N:
        print("%d = " %(N),end="")
        for i in range(len(divisor)-1):
            print("%d + " %(divisor[i]) ,end="")
        print(divisor[-1])
    else:
        print("%d is NOT perfect." %(N))