import sys
input=sys.stdin.readline

def check(depth):
    if len(answer_check)==L:
        cnt=0
        for i in range(L-1):
            if (answer_check[i] in 'aeiou') or (answer_check[L-1] in 'aeiou'):
                cnt+=1
            if ord(answer_check[i]) >= ord(answer_check[i+1]):
                break
            if (i ==L-2) and cnt!=0:
                print(''.join(answer_check))
        return

    for i in range(C):
            answer_check.append(word[i])
            check(depth+1)
            answer_check.pop()

L,C=map(int,input().split())
word=sorted(list(map(str,input().split())))
answer_check=[]
check(0)