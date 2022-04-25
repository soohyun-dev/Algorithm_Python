N=int(input())

a=1
b=1
c=0

if N==1:
    print(a)
elif N==2:
    print(b)
else:
    for i in range(N-2):
        c=a+b
        a=b
        b=c
    print(c)