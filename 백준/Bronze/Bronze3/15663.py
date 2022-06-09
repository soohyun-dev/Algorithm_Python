N=int(input())
if N==1:
    S=1
else:
    total=[1,N]
    for i in range(2,N//2+1):
        if N%i==0:
            total.append(i)
    S=sum(total)
print((S*5)-24)