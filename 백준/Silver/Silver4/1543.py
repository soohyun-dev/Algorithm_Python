import sys
input=sys.stdin.readline

doc=input().rstrip()
ex=input().rstrip()
cnt=0
i=0

while i <= len(doc)-len(ex):
    print(doc[i:i+len(ex)], ex)
    if doc[i:i+len(ex)]==ex:
        cnt+=1
        i+=len(ex)
    else:
        i+=1
print(cnt) 