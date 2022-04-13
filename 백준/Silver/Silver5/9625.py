K=int(input())
A=[1,0]
B=[0,1]

for i in range(1,K):
    a,b=B[0],B[1]
    B[0]+=A[0]
    B[1]+=A[1]
    A=[a,b]

print(B[0],B[1])


