Max=0      # 최댓값
column=0   # 행
row=0      # 열
for i in range(1,10):
  line = list(map(int,input().split()))
  if (Max<max(line)):  # 최댓값 찾기
    Max=max(line)
    column=i
    row=line.index(Max)  
print(Max)
print(column, row+1)


