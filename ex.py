from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
    visited[0][0] = [1] * (k+1)

    while q:
        x, y, c = q.popleft()  # 좌표와 벽을 부술 수 있는 남은 횟수
        if x == n - 1 and y == m - 1:
            for i in range(n):
                print(visited[i])
            return visited[x][y][c]
        nextVisited = visited[x][y][c] + 1

        for i in range(4):
            tx = dx[i] + x
            ty = dy[i] + y
            if 0 <= tx < n and 0 <= ty < m and not visited[tx][ty][c]:
                if not a[tx][ty]:  # 빈 방이라면
                    visited[tx][ty][c] = nextVisited
                    q.append([tx, ty, c])

                elif c < k:  # 벽을 아직 부술 수 있음
                    visited[tx][ty][c + 1] = nextVisited
                    q.append([tx, ty, c + 1])  # c를 -1해서 저장
    return -1

n, m, k = map(int, input().split())
a = [list(map(int, input().strip())) for _ in range(n)]

print(bfs())
