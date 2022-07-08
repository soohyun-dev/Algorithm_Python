N=int(input())
house=sorted(list(map(int,input().split())))

if N<3:
    print(house[0])
else:
    center=N//2
    check=center
    if N%2==0:
        center-=1
        total=sum(house)
        for i in range(2):
            result=0
            for j in range(N):
                result+=abs(house[j]-house[center])
            if result<total:
                total=result
                check=center
            center+=1
                
    print(house[check])

    



