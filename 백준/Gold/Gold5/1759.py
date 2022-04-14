import sys
input=sys.stdin.readline

def cnt(W):  # 모음, 자음 카운트 함수
    Vow=0
    Con=0
    for i in range(L):
        if W[i] in 'aeiou':
            Vow+=1  # 모음 수 카운트
        else:
            Con+=1  # 자음 수 카운트
    if Vow>=1 and Con>=2:
        return True
    return

def check(idx,depth):
    if len(answer_check)==L:
        if cnt(answer_check)==True:  # 모음, 자음 체크
            print(''.join(answer_check))
        return
    for i in range(idx,C):
        if not visited[i]:
            answer_check.append(word[i])
            visited[i]=True
            check(i+1,depth+1)
            visited[i]=False
            answer_check.pop()

L,C=map(int,input().split())
word=sorted(input().split())
answer_check=[]
visited=[False]*(C+1)
check(0,0)


