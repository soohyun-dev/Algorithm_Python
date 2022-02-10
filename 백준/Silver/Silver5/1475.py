N=str(input())
cnt=[0]*10
for i in range(len(N)):
    if N[i]=='6' or N[i]=='9':
        cnt[6]+=1
    else:
        cnt[int(N[i])]+=1

if cnt[6]%2==0:
    cnt[6]=cnt[6]//2
elif cnt[6]%2!=0:
    cnt[6]=(cnt[6]//2)+1

print(max(cnt))


