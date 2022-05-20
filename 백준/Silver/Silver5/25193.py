N=int(input())
l=list(input())
cnt=0
for i in range(N):
    if l[i]!='C':
        cnt+=1

tmp=N-cnt
if cnt==0:
    print(N)
elif (tmp%cnt)!=0:
    if tmp//cnt >3:
        print((tmp//cnt)-1)
    else:
        print(tmp//cnt)
else:
    print(tmp//(cnt+1))  
    