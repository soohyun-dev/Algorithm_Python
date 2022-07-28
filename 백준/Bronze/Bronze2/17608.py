import sys
input=sys.stdin.readline

N=int(input())
l=[]
for i in range(N):
    stick=int(input())
    while True:
        if len(l)>0:
            if l[-1] <= stick:
                l.pop()
            else:
                l.append(stick)
                break
        else:
            l.append(stick)
            break
                
print(len(l))