N=int(input())
A=[1,2,3,4,5,6]
B=[1,2,3,4,5,6]
for i in A:
    for j in B:
        if i+j==N:
            print(i,j)