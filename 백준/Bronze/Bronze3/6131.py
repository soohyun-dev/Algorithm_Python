num=int(input())
cnt=0

for i in range(1,501):
    for j in range(1,i):
        if (i*i)-(j*j)==num:
            cnt+=1

print(cnt)