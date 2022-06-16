for _ in range(int(input())):
    n,m = map(int,input().split())
    cnt=0
    for i in range(2,n):
        for j in range(1,i):
            if (i**2+j**2+m)%(i*j)==0:
                cnt+=1      
    print(cnt)
    