N=int(input())
for i in range(N):
    print(' '*(N-i-1)+'*'+' '*(i*2)+'*')
for j in range(N-2,-1,-1):
    print(' '*(N-j-1)+'*'+' '*(j*2)+'*')