for i in range(3):
    l=list(map(str,input().split()))
    cnt=l.count('1')
    if cnt==0:
        print('D')
    elif cnt==1:
        print('C')
    elif cnt==2:
        print('B')
    elif cnt==3:
        print('A')
    elif cnt==4:
        print('E')


