import sys
input=sys.stdin.readline

n,k = map(int,input().split())
l=[1,2,3]
answer=[]

def check(answer_check):
    if sum(answer_check)>n:
        return
    if sum(answer_check)==n:
        a='+'.join(map(str,answer_check))
        if a not in answer:
            answer.append(a)
            return

    for i in range(3):
        answer_check.append(l[i])
        check(answer_check)
        answer_check.pop()

check([])
if len(answer)>=k:
    print(answer[k-1])
else:
    print(-1)




