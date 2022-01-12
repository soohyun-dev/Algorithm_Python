import sys
input = sys.stdin.readline

N = int(input())
list = sorted([int(input()) for _ in range(N)], reverse = True)
for i in range(N):
  print(list[i])

  