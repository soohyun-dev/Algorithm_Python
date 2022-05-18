import sys
input=sys.stdin.readline

N=int(input())
check=[False]*(N+1)
record=[[0]]  # 인덱스 맞춰주기 위함.
for i in range(N):
    record.append(list(map(int,input().split())))

prize=[]
n=200001

for i in range(1,5):
    max=-1
    for j in range(1,N+1):
        if check[record[j][0]]==False:  # 앞에서 상품을 받은 사람은 패스
            
            if record[j][i] > max:  
                if check[record[j][0]]==False:
                    max=record[j][i]
                    n=record[j][0]
                    
            elif record[j][i] == max:  # 동점일 경우 둘 중 작은 번호를 우선으로 함.
                n=min(n, record[j][0])
                
    prize.append(n)
    check[n]=True  # 상품 줬다 표시

print(*prize)





