import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
start, end = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, weight = map(int, input().split())
    arr[a].append((weight, b))
    arr[b].append((weight, a))
visited = [0] * (N+1)


def dijkstra():
    q = []
    heapq.heappush(q, (-sys.maxsize, start))
    visited[start] = sys.maxsize
    while q:
        cost, node = heapq.heappop(q)
        cost = -cost
        if visited[node] > cost:
            continue
        for ncost, nnode in arr[node]:
            temp = min(cost, ncost)
            if visited[nnode] < temp:
                visited[nnode] = temp
                heapq.heappush(q, (-temp, nnode))


dijkstra()
print(visited[end])
 