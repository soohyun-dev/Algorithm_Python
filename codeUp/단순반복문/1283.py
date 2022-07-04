a=int(input())
b=int(input())
tmp=a
data=list(map(int,input().split()))
for i in range(b):
    if data[i]>0:
        a*=((100+data[i])/100)
    elif data[i]<0:
        a*=((100+data[i])/100)
        
result=int(f'{a:.0f}')
if tmp==result:
    print(0)
    print('same')
elif tmp>result:
    print(result-tmp)
    print('bad')
elif tmp<result:
    print(result-tmp)
    print('good')
    
    