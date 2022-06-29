n,m=map(int,input().split())
for i in range(m):
    if i==0 or i==m-1:
        print('+'+'-'*(n-2)+'+')
    else:
        print('|'+' '*(n-2)+'|')
    