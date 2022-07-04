import collections

width,length=map(int,input().split())
paper=[[0]*width for _ in range(length)]
N=int(input())
for i in range(N):
    direction,num=map(int,input().split())
    for j in range(length):
        for k in range(width):
            if direction==0:
                if j>=num:
                    paper[j][k]+=1
            if direction==1:
                if k>=num:
                    paper[j][k]+=100

store={}
store=collections.Counter(store)
for l in range(length):
    dict={}
    dict=collections.Counter(paper[l])
    store+=dict
    
print(max(store.values()))

for i in range(length):
    print(*paper[i])
