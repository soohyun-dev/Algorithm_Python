import heapq
import sys
input=sys.stdin.readline

height=[]

for _ in range(9):
    height.append(int(input()))

answer=[]    
answer_check=[]
visited=[False]*9

def check(depth):
    global answer
    if len(answer_check)==7:
        if sum(answer_check)==100 and answer_check!=answer:
            answer_check.sort()
            answer=answer_check
            for i in range(7):
                print(answer_check[i])
        return
    
    for i in range(9):
        if not visited[i]:
            answer_check.append(height[i])
            visited[i]=True
            check(depth+1)
            answer_check.pop()
            visited[i]=False

check(0)
        
    