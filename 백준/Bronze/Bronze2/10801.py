A=list(map(int,input().split()))
B=list(map(int,input().split()))
A_cnt,B_cnt=0,0
for i in range(10):
    if A[i]>B[i]:
        A_cnt+=1
    elif A[i]<B[i]:
        B_cnt+=1
        
if A_cnt>B_cnt:
    print('A')
elif A_cnt<B_cnt:
    print('B')
else:
    print('D')
    