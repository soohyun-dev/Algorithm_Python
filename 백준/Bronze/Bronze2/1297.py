a,b,c=map(int,input().split())
tmp=(b**2 + c**2)**(1/2)
v=a/tmp
print(int(b*v),int(c*v))