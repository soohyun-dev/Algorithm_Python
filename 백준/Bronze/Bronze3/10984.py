for i in range(int(input())):
  cs=0
  gs=0
  cnt=int(input())
  for j in range(cnt):
    C,G=map(float, input().split())
    cs+=C
    gs+=float(C*G)
  grade=gs/cs
  print(int(cs), '%.1f' %grade)