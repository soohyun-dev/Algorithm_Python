k=list(input())
left=0
right=0
for i in range(len(k)):
    if k[i]=='(':
        left+=1
    elif k[i]==')':
        right+=1
        
print(left,right)