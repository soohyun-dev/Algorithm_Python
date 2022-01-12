import sys

def dfs(start):
  global cnt
  visited[start] = True
  for i in graph[start]:
    if not visited[i]:
      dfs(i)
      cnt+=1 

computer = int(input())
N = int(input())
cnt=0
graph = [[] * computer for i in range(computer+1)]
for i in range(N):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)
visited = [0] * (computer+1)

dfs(1)
print(cnt)
