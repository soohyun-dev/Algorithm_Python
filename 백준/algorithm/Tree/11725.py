import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N=int(input())
Tree = [[] for _ in range(N+1)]
check=[0]*(N+1)

def DFS(N):
  for i in Tree[N]:
    if check[i] == 0:
      check[i]=N
      DFS(i)

for i in range(N-1):
  node_1, node_2=map(int,input().split())
  Tree[node_1].append(node_2)
  Tree[node_2].append(node_1)

DFS(1)
for i in range(2, N+1):
  print(check[i])



'''
N=int(input())
Tree={}
node_1 ,node_2 = map(str, input().split())
visitied=[False]*(N+1)

if node_1=='1':
  Tree[node_1]=[node_2]
  visitied[int(node_1)]=True
  visitied[int(node_2)]=True

for i in range(N-2):
  node_1 ,node_2 = map(str, input().split())

  if node_1 in Tree.keys():
    Tree[node_1].append(node_2)
    visitied[int(node_1)]=True
    visitied[int(node_2)]=True
  elif node_2 in Tree.keys():
    Tree[node_2].append(node_1)
    visitied[int(node_1)]=True
    visitied[int(node_2)]=True
  else:
    if visitied[int(node_1)]==True:
      Tree[node_1]=[node_2]
    elif visitied[int(node_2)]==True:
      Tree[node_2]=[node_1]
    else:
      Tree[node_1]=[node_2]
  
def get_key(val):
  for key, value in Tree.items():
    if str(val) in value:
      return key

for i in range(2,N+1):
  print(get_key(i))


'''