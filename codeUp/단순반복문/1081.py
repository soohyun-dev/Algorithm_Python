N=int(input())
for i in range(1,N+1):
    if i==3 or i==6 or i==9:
        print('X', end=' ')
    else:
        print(i, end=' ')