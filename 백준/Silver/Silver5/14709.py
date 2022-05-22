N=int(input())
finger=[[]]
check=True
for i in range(5):
    finger.append([])
for i in range(N):
    a,b=map(int,input().split())
    finger[a].append(b)
    finger[b].append(a)
    
if (3 and 4  not in finger[1]) or len(finger[1])!=2:
    check=False
elif (1 and 4  not in finger[3]) or len(finger[3])!=2:
    check=False
elif (1 and 3  not in finger[4]) or len(finger[4])!=2:
    check=False
    
if check==True:
    print('Wa-pa-pa-pa-pa-pa-pow!')
else:
    print('Woof-meow-tweet-squeek')
    