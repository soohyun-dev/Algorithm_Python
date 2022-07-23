N=int(input())
graph=[]
for i in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][k]==1 or (graph[j][i]==1 and graph[i][k]==1):
                graph[j][k]=1
        
    for l in range(N):
        print(*graph[l])
    print()