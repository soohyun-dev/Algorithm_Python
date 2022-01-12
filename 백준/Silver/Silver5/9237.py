import sys

N=int(input())
day=list(map(int, sys.stdin.readline().split()))
day.sort(reverse=True)

for i in range(len(day)):
  day[i]= day[i] + i + 1
print(max(day) + 1)