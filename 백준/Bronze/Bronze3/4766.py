import sys
input=sys.stdin.readline

l=[]
while True:
    num=float(input())
    if num==999:
        break
    l.append(num)

for i in range(1,len(l)):
    print(format(l[i]-l[i-1],".2f"))