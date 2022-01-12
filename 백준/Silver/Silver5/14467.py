N=int(input())
l=['x']*11
cnt=0
for i in range(N):
    cow, num = map(int,input().split())
    if l[cow] == 'x':
        l[cow]=num
    else:
        if l[cow]==num:
            continue
        elif l[cow] != num:
            l[cow] = num
            cnt+=1
print(cnt)