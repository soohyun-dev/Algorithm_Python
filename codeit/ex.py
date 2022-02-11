import sys
input=sys.stdin.readline


for i in range(int(input())):
    l=[1,2,3]
    n=int(input())
    cnt=0

    def check(answer_check):
        global cnt
        if sum(answer_check)>n:
            return
        if sum(answer_check)==n:
            cnt+=1
            return
            
        for i in range(3):
            answer_check.append(l[i])
            check(answer_check)
            answer_check.pop()

    check([])

    print(cnt%1000000009)


