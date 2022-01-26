import sys
input = sys.stdin.readline

def pre(now_node):  # 전위 순회
  if now_node == '.':  # 자식이 없는 경우
    return
  else:
    print(now_node, end='')
    left, right = Tree[now_node]
    pre(left)
    pre(right)

def mid(now_node):  # 중위 순회
  if now_node == '.':  # 자식이 없는 경우
    return
  else:
    left, right = Tree[now_node]
    mid(left)
    print(now_node, end='')
    mid(right)

def post(now_node):  # 후위 순회
  if now_node == '.':  # 자식이 없는 경우
    return
  else:
    left, right = Tree[now_node]
    post(left)
    post(right)
    print(now_node, end='')

Tree={}
N=int(input())
for i in range(N):
  parent, left_child, right_child = map(str,input().split())
  Tree[parent] = [left_child, right_child]

pre('A')
print()
mid('A')
print()
post('A')







