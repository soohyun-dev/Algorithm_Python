import sys
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline


n, m = map(int, input().split())
L = defaultdict(list)
for i in range(m):
    a, b, c = map(int, input().split())
    L[a].append((b, c))
    L[b].append((a, c))
x, y, z = map(int, input().split())


def dijkstra(S):
    Q = list()
    heappush(Q, (0, S))

    D = [float('inf')] * (n + 1)
    D[S] = 0
    
    P = defaultdict(int)

    while Q:
        SD, SN = heappop(Q)

        if D[SN] < SD:
            continue
        
        for FN, FD in L[SN]:
            d = SD + FD
            if D[FN] > d:
                D[FN] = d
                heappush(Q, (d, FN))
                P[FN] = SN

    return D, P

def link(index, S, P):
    temp, L = index, []
    while temp != S:
        L.append((P[temp], temp))
        temp = P[temp]
    return L


D1, P1 = dijkstra(x)
D2, P2 = dijkstra(y)
D3, P3 = dijkstra(z)
print(D1)
print(D2)
print(D3)
index, dist = 0, float('inf')
for i in range(1, n + 1):
    if D1[i] + D2[i] + D3[i] < dist:
        index = i
        dist = D1[i] + D2[i] + D3[i]

R = list()
R += link(index, x, P1)
R += link(index, y, P2)
R += link(index, z, P3)

print(dist, len(R))
for x, y in R:
    print(x, y)