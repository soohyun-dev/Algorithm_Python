n, m = map(int, input().split())
my_list = list(map(int, input().split()))
my_list.sort()
visited = [False] * n
solve = []

def Dfs(depth):
    if m == depth:
        print(' '.join(map(str, solve)))
        return

    for i in range(n):
        if not visited[i]:
            if depth == 0 or solve[depth - 1] < my_list[i]:
                solve.append(my_list[i])
                visited[i] = True
                Dfs(depth + 1)
                visited[i] = False
                solve.pop()

Dfs(0)