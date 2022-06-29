n=input()
m=int(n,16)
for i in range(1,16):
    print('%s*%s=%s' %(n,format(i,'X'), format(m*i, 'X')))