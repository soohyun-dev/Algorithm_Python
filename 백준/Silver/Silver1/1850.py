def gcd(a,b):
    if b!=0:
        tmp=a%b
        return gcd(b,tmp)
    else: 
        return a
A,B=map(int,input().split())
cnt=gcd(A,B)
print(cnt)
print('1'*cnt)
    