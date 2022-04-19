import sys
input=sys.stdin.readline

while True:
    try:
        N,M=map(int,input().split())
    except: 
        break
    sum=0
    for num in range(N,M+1):
        num=list(str(num))
        num.sort()
        check=True
        for i in range(len(num)-1):
            if num[i]==num[i+1]:
                check=False
                break
        if check==True:
            sum+=1
    print(sum)
 