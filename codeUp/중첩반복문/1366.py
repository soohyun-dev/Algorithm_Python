N=int(input())
cut=N//2

for i in range(cut):
    if i==0:
        print('*'*N)
    else:
        print('*'+' '*(i-1)+'*'+' '*((N-2-(2*i))//2)+'*'+' '*((N-2-(2*i))//2)+'*'+' '*(i-1)+'*')

print('*'*N)
    

for i in range(cut-1,-1,-1):
    if i==0:
        print('*'*N)
    else:
        print('*'+' '*(i-1)+'*'+' '*((N-2-(2*i))//2)+'*'+' '*((N-2-(2*i))//2)+'*'+' '*(i-1)+'*')