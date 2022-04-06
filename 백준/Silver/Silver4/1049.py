import sys
input=sys.stdin.readline

N,M=map(int,input().split())
store=[999,999]
for i in range(M):
    pack,each=map(int,input().split())
    store[0]=min(store[0],pack)
    store[1]=min(store[1],each)
qu=N//6  # 몫
re=N%6  # 나머지
price=(qu*store[0])+(re*store[1]) # 몫만큼 패키지를 사고, 나머지 만큼 낱개로 살때
tmp=N*store[1]  # 낱개로만 샀을때

if re!=0:
    qu+=1
price=min(price, tmp, store[0]*qu)  # 패키지만 살 때 와  위 두 값을 비교

print(price)

