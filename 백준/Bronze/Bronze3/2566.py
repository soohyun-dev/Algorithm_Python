Max=0      # 최댓값
column=0   # 행
row=0      # 열
for i in range(9):
    l=list(map(int,input().split()))
    for j in range(9):
        if l[j]>Max:
            Max=l[j]
            column=i+1
            row=j+1
print(Max)
if Max==0:
    print(1,1)
else:
    print(column, row)

