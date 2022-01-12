N=int(input())
for i in range(N):
  l=list(map(int, input().split()))
  l.sort()
  if l[3]-l[1] >=4:
    print('KIN')
  else:
    print(sum(l[1:4]))


