import sys
input=sys.stdin.readline

N,H,W=map(int,input().split())
word=[]
for i in range(H):
    word.append(list(input().rstrip()))
original=[]

for i in range(N):
    check=False
    for j in range(H):
        for k in range(W):
            if word[j][k]!='?':
                original.append(word[j][k])
                check=True
                break    
        if check==True:
            break
        elif check==False and j==H-1 and k==W-1:
            original.append('?')
            break
    if i != N-1:
        for l in range(H):
            for m in range(W):
                del word[l][0]
print(*original, sep='')         