import sys
input=sys.stdin.readline

N=int(input())
words=[input().rstrip('\n') for  _ in range(N)]
words.sort()
sum=0
for i in range(N):
    check=True
    for j in range(i+1,N):
        if words[i]==words[j][0:len(words[i])]:
            check=False
            break
        
    if check:
        sum+=1
        
print(sum)