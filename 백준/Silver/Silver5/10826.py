def fibo(num):
    check=[0]*(num+1)
    check[1]=1
    for i in range(1,num):
        check[i+1]+=check[i]+check[i-1]
        
    return check
N=int(input())
if N==0:
    print(0)
else:
    fibonacci=fibo(N)
    print(fibonacci[N])
    
    
    