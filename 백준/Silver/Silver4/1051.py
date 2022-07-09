N,M=map(int,input().split())
l=[]
cnt=N-1
for i in range(N):
    l.append(list(map(int,input())))
    
check=False

while True:
    for i in range(N-cnt):
        for j in range(M-cnt):
            if l[i][j]==l[i][j+cnt]==l[i+cnt][j]==l[i+cnt][j+cnt]:
                print((cnt+1)*(cnt+1))
                check=True
                break
        if check==True:
            break
    cnt-=1
    if check==True or cnt==0:
        break

if check==False:
    print(1)
    
    