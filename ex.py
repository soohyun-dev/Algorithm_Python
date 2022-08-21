import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
g = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, w = map(int, input().split())
    g[a].append((w, b))
    g[b].append((w, a))


q = g[1] 
visited = [True, True] + [False]*(v-1)
heapq.heapify(q)
answer = 0
while q:
    w, dest = heapq.heappop(q)
    if not visited[dest]:
        visited[dest] = True
        answer += w
        for e in g[dest]:
            if not visited[e[1]]:
                heapq.heappush(q, e) 
print(answer)