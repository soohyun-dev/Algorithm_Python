import sys
input=sys.stdin.readline

for i in range(int(input())):
    n=int(input())
    answer=[]

    def check(answer_check):
        if sum(answer_check)>n:
            return
        if sum(answer_check)==n:
            a='+'.join(map(str,answer_check))
            if a not in answer:
                answer.append(a)
                return

        for i in range(1,4):
            answer_check.append(i)
            check(answer_check)
            answer_check.pop()

    check([])

    print(len(answer))

