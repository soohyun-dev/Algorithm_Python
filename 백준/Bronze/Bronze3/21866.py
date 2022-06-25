score=list(map(int,input().split()))
M=[100,100,200,200,300,300,400,400,500]
check=True
sum=0

for i in range(9):
    sum+=score[i]
    if M[i]-score[i]<0:
        check=False
        break

if check==False:
    print('hacker')
elif sum==100:
    print('draw')
elif sum<100:
    print('none')