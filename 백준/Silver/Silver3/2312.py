import sys
input=sys.stdin.readline

N=int(input())
for i in range(N):
    num=int(input())
    a=2
    cnt=[]
    while a<=num:
        if num%a==0:
            num//=a
            cnt.append(a)
        else:
            a+=1
    cnt.sort()
    tmp=set(cnt)
    value=sorted(list(tmp))

    for i in range(len(value)):
        print(value[i],cnt.count(value[i]))
     
     