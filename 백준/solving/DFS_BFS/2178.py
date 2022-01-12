from collections import deque

def bfs(x,y):
  queue = deque()  # deque 라이브러리 사용
  queue.append((x,y))  # 현재 위치를 추가
  while queue:  # queue 가 빌 때까지 반복
    x,y=queue.popleft()  
    for i in range(4):
      nx = x + dx[i]  # 상, 하, 좌, 우 탐색
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 벽을 넘어가는 경우 무시
        continue
      if graph[nx][ny]==0:  # 벽인 경우 무시
        continue
      # 해당 노드를 처음 방문하는 경우일 때 최단 거리를 기록
      if graph[nx][ny]==1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
  return graph[n-1][m-1]


n,m=map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))

