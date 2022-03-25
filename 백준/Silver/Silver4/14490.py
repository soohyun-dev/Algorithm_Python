N,M=map(int,input().split(':'))
a=N
b=M

while b>0:
    value=a
    a=b
    b=value%b
print('%d:%d' %(N//a, M//a))
    