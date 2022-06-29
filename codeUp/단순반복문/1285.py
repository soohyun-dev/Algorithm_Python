express=input()
l=[]
tmp=[]
for i in range(len(express)):
    express[i].isdigit()
    if express[i].isdigit()==True:
        tmp.append(express[i])
    else:

        l.append(int("".join(tmp)))
        tmp=[]
        l.append(express[i])
cnt=1
result=int(l[0])
while True:
    if l[cnt]=='=':
        break
    if l[cnt]=='+':
        cnt+=1
        result+=int(l[cnt])
        cnt+=1
    elif l[cnt]=='-':
        cnt+=1
        result-=int(l[cnt])
        cnt+=1
    elif l[cnt]=='*':
        cnt+=1
        result*=int(l[cnt])
        cnt+=1
    elif l[cnt]=='/':
        cnt+=1
        result//=int(l[cnt])
        cnt+=1
        
print(result)
    