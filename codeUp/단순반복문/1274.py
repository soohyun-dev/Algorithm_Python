def aristo(index):
    ari=[True]*(index+1)
    ari[0],ari[1]=False,False
    
    for i in range(2,index//2+1):
        if ari[i]==True:
            for j in range(i+i,index+1,i):
                ari[j]=False
    return ari

ari=aristo(1000000)
N=int(input())

if ari[N]==False:
    print('not prime')
else:
    print('prime')