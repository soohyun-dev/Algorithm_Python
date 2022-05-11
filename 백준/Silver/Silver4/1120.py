A,B = input().split()

tmp=len(B)-len(A)
answer=50
for i in range(tmp+1):
    sum=0
    store = ('0'*i) + A + ('0'*(tmp-i))
    for i in range(len(B)):
        if store[i]!=B[i]:
            sum+=1
    sum-=tmp
    if answer > sum:
        answer=sum

print(answer)




