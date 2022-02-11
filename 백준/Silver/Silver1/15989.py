import sys
input=sys.stdin.readline

def check(answer_checked):
    if sum(answer_checked)>n:
        return
    if sum(answer_checked)==n:
        a=str(sorted(answer_checked))    
        answer.append(a)

    for i in range(1,4):
        answer_checked.append(i)
        check(answer_checked)
        answer_checked.pop()



for i in range(int(input())):
    n=int(input())
    answer=[]
    check([])
    answer=set(answer)
    print(len(answer))
