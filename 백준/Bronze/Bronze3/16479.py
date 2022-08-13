N=int(input())
x,y=map(int,input().split())
h=N**2-(abs(x-y)/2)**2
print("%g" %(h))