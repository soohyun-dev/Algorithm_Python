L=int(input())
S=list(map(int,input().split()))
S.append(0)
S.sort()
n=int(input())
cnt=0
for i in range(L):
    if S[i]==n:
        break
    else:
        if S[i]<n and n<S[i+1]:
            cnt=((n-S[i])*(S[i+1]-n))-1
            break

print(cnt)