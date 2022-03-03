import sys 
input=sys.stdin.readline

N=int(input())
num=list(map(int,input().split()))
store=[]
tmp=0
check=True  

if num[0]>=0:
    tmp+=num[0]
else:
    tmp+=num[0]
    check=False
    store.append(num[0])

for i in range(1,N):
    if num[i]<0 and check==True:
        store.append(tmp)
        tmp=0
        check=False
    elif num[i]>0 and check==False:
        store.append(tmp)
        tmp=0
        check=True
    tmp+=num[i]

    if i==N-1 and num[-1]>0:
        store.append(tmp)

print(store)

if len(store)==1 and check==False:  # num 리스트에 음수밖에 없을 때
    print(max(num))
else:
    sum=store[0]
    m=[sum]
    for i in range(1,len(store)):
        if sum+store[i]<0:
            sum=0
        else:
            sum=sum+store[i]
            m.append(sum)

    print(max(m))


