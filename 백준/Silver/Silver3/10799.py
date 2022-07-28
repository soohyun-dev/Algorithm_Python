LIST=list(input())
store=[]
check=False
result=0
for i in LIST:
    if i=='(':
        store.append(1)
        check=True
    elif i==')':
        if check==True:
            store.pop()
            check=False
            result+=len(store)
        else:
            store.pop()
            result+=1
            
print(result)
    