N=list(input())
cnt=0
while len(N)>1:
    tmp=1
    for i in range(len(N)):
        tmp*=int(N[i])
    N=list(str(tmp))
    cnt+=1
print(cnt)