N,kim,lim=map(int,input().split())
cnt=0

while True:
    kim-=kim//2
    lim-=lim//2
    cnt+=1
    if kim==lim:
        print(cnt)
        break

