a,b=map(int,input().split())
x,y=a//b,a%b
if a!=0 and y<0:
    x,y=x+1,b-y
print(x)
print(y)