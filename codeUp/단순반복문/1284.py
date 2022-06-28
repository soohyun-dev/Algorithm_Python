def aristo(index):
    ari=[True]*(index+1)
    ari[0],ari[1]=False,False
    
    for i in range(2,index//2+1):
        if ari[i]==True:
            for j in range(i+i,index+1,i):
                ari[j]=False
                
    return ari

N=int(input())
tmp=False

if N!=1:
    check=aristo(N//2)
    divisor=[]

    for i in range(2,N//2+1):
        if N%i==0:
            divisor.append(i)
            
    for j in range(len(divisor)//2):
        if check[divisor[j]]==True and check[divisor[len(divisor)-j-1]]==True:
            print(divisor[j], divisor[len(divisor)-j-1])
            tmp=True
            break

if tmp==False:
    print('wrong number')
    
        
    
