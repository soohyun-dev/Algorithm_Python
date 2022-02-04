import sys
input=sys.stdin.readline

N=int(input())
province=list(map(int,input().split()))
budget=int(input())


low, high = 0, max(province)

if sum(province)<=budget:
    print(max(province))
else:
    while low <= high :
        divide=(low+high)//2
        total=0

        for amount in province:
            if amount >= divide:
                total+=divide
            else:
                total+=amount

        if total <= budget:
            low=divide+1
        else:
            high=divide-1

    print(high)


