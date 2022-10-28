import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    S=list(input())
    N=int(input())
    Nums=input().rstrip()[1:-1].split(',')
    RUR=False
    check=True
    startIdx=0
    delCnt=0
    if (N==0):
        Nums=[]
    for v in S:
        if (v=='R'):
            RUR= not RUR
        elif (v=='D') :
            if (startIdx+delCnt>=len(Nums)):
                check=False
                break
            else:
                if (RUR):
                    Nums.pop()
                    delCnt+=1
                else: 
                    startIdx+=1
            
    Nums=Nums[startIdx:]
    if (RUR): Nums.reverse()
    if (check==True) :
        print('['+','.join(Nums)+']')
    else :
        print('error')