from collections import deque
import sys

D=deque()
N=int(input())

def size():
  return len(D)

def empty():
  if len(D)==0:
    return 1
  else:
    return 0

def front():
  if(len(D)==0):
    return -1
  else:
    return D[0]

def back():
  if(len(D)==0):
    return -1
  else:
    return D[-1]
    
for i in range(N):
  order=list(sys.stdin.readline().split())

  if order[0]=="push_front":
    D.appendleft(order[1])
  elif order[0]=="push_back":
    D.append(order[1])
  elif order[0]=="pop_front":
    if len(D)==0:
      print(-1)
    else:
      f=D.popleft()
      print(f)
  elif order[0]=="pop_back":
    if len(D)==0:
      print(-1)
    else:
      b=D.pop()
      print(b)
  elif order[0]=="size":
    print(size())
  elif order[0]=="empty":
    print(empty())
  elif order[0]=="front":
    print(front())
  elif order[0]=="back":
    print(back())




