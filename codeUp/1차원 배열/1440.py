N=int(input())
nums=list(map(int,input().split()))

for i in range(N):
    buho=[]
    tmp=nums[i]
    tmp_list=[]
    for k in range(N):
        if i!=k:
            tmp_list.append(nums[k])
    for j in range(N-1):
        if tmp==tmp_list[j]:
            buho.append('=')
        elif tmp>tmp_list[j]:
            buho.append('>')
        elif tmp<tmp_list[j]:
            buho.append('<')
    print('%d: ' %(i+1), end='')
    for m in range(N-1):
        print(buho[m], end=' ')
    print()