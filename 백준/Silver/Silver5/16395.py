n,k=map(int,input().split())
pascal=[[1],[1,2,1]]
for i in range(1,n-1):
    tmp=[1]
    for j in range(len(pascal[i])):
        tmp.append(sum(pascal[i][j:j+2]))
    pascal.append(tmp)

print(pascal)
print(pascal[n-2][k-1])



