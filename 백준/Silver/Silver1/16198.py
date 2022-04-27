def check(depth):
    global energy

    if len(W)==2:
        if depth>energy:
            energy=depth
        return
    for i in range(1,len(W)-1):
        tmp=W[i-1]*W[i+1]
        store=W[i]
        W.remove(W[i])
        check(tmp+depth)
        W.insert(i, store)

N=int(input())
W=list(map(int,input().split()))
energy=0
check(0)
print(energy)