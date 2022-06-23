N=int(input())
road=list(map(int,input().split()))
city=list(map(int,input().split()))
result=0
c=sorted(city, key=lambda x:-x)

if city==c:  # 최악의 케이스인 경우
    for i in range(len(road)):
        result+=road[i]*city[i]
    print(result)
else:
    while True:
        tmp=min(city)
        for i in range(len(city)):
            if city[i]==tmp:
                s=sum(road[i:])
                result+=(s*tmp)
                del(city[i:])
                del(road[i:])
                break
        if len(city)==0:
            print(result)
            break
    
