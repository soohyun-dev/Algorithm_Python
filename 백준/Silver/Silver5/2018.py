# N=int(input())
# a,b=0,1
# cnt=0
# v=1
# while b<=N and a<=b:
#     if v==N:
#         cnt+=1
#         b+=1
#         v=v-a+b
#         a+=1
#     elif v<N:
#         b+=1
#         v+=b
#     else:
#         v-=a
#         a+=1
# print(cnt) 

N=int(input())
cnt=0
if N==1:
    print(1)
else:
    for i in range(1,N+1):
        sum=0
        tmp=i
        while True:
            sum+=tmp
            tmp+=1
            if sum>N:
                break
            elif sum==N:
                cnt+=1
                break
    print(cnt)