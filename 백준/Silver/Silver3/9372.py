import sys
input = sys.stdin.readline

def dfs(cnt, idx):
    check[idx]=True

    for i in graph[idx]:
        if check[i]==False:
            cnt=dfs(cnt+1,i)
        
    return cnt


T=int(input())

for _ in range(T):
    N,M=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    check=[False]*(N+1)

    for j in range(M):
        left_node, right_node = map(int, input().split())
        graph[left_node].append(right_node)
        graph[right_node].append(left_node)

    answer=dfs(0,1)
    print(answer)



