l=[0, 1, 1]
for i in range(1, 81):
    tmp=l[i+1]+l[i]
    l.append(tmp)
N=int(input())
sum=(l[N]*4)+(l[N-1]*2)
print(sum)


