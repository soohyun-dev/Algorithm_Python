import sys
input=sys.stdin.readline

N=int(input())
words=[input().rstrip('\n') for _ in range(N)]
words.sort()
store=[[]for _ in range(N)]
store[0]=[words[0]]
result=1
cnt=0

for i in range(1,N):
    if words[i-1]==words[i][0:len(words[i-1])]:
        store[cnt].append(words[i])
    else:
        cnt+=1
        store[cnt].append(words[i])
        result+=1

print(store)
print(result)


