N=int(input())
answer=[]
for i in range(N+1):
    l=[N] 
    tmp=N  
    a=i
    while True:
        store=tmp-a  
        if store<0:
            l.append(a)  
            break
        else:
            l.append(a)  
            tmp=a
            a=store
    if len(l)>len(answer):
        answer=l
print(len(answer))
print(*answer)


