n,k=map(int,input().split())
tmp=n-k
down=1
up=1

if k>=tmp:
    a=k
    b=tmp
else:
    a=tmp
    b=k 
    
for i in range(2,a+1):
    down*=i
for j in range(b+1,n+1):
    up*=j
    
result=(up//down)%10007
print(result)

