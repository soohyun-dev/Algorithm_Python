wool=list(map(int,input().split()))
start=list(map(int,input().split()))
wool_cnt=0
start_cnt=0
check=False

for i in range(9):
    wool_cnt+=wool[i]
    if wool_cnt>start_cnt:
        check=True
    start_cnt+=start[i]

if check==True and wool_cnt<start_cnt:
    print('Yes')
else:
    print('No')