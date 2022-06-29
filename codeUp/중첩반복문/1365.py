N=int(input())
cut=N//2

for i in range(cut):
    if i==0:
        print('*'*N)
    else:
        print('*'+' '*(i-1)+'*'+' '*(N-2-(2*i))+'*'+' '*(i-1)+'*')

if N%2!=0: # 가운데 중점, 짝수일 경우 X
    print('*'+' '*(cut-1)+'*'+' '*(cut-1)+'*')
    

for i in range(cut-1,-1,-1):
    if i==0:
        print('*'*N)
    else:
        print('*'+' '*(i-1)+'*'+' '*(N-2-(2*i))+'*'+' '*(i-1)+'*')
    
    
    
