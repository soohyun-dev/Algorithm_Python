R,C,W=map(int,input().split())
pascal=[[1],[1,1]]
for i in range(1,R+W-1):
    tmp=[1]
    for j in range(len(pascal[i])):
        tmp.append(sum(pascal[i][j:j+2]))
    pascal.append(tmp)

sum=pascal[R-1][C-1]
for j in range(1,W):
    cnt=C-1
    for k in range(j+1):
        sum+=pascal[R][cnt]
        print(pascal[R][cnt])
        cnt+=1
    R+=1
print(sum)