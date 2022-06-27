a,b,c=map(int,input().split())
m=max(a,b,c)
tmp=m
while True:
    if m%a==0 and m%b==0 and m%c==0:
        print(m)
        break
    m+=tmp