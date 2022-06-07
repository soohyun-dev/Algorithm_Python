l=[]
for i in range(1,21):
    l.append(i)

for j in range(10):
    start,end=map(int,input().split())
    l[start-1:end]=list(reversed(l[start-1:end]))

print(*l)