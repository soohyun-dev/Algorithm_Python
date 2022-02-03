import sys
from collections import Counter
input=sys.stdin.readline

l=[]
N=int(input())
for i in range(N):
  l.append(int(input()))
l.sort()
# 산술평균
print(round(sum(l)/N))

# 중앙값
print(l[N//2])

# 최빈값
cnt=Counter(l).most_common()
if len(l)!=1:
  if cnt[0][1]==cnt[1][1]:
    print(cnt[1][0])
  else:
    print(cnt[0][0])
else:
  print(l[0])

# 범위
print(l[-1]-l[0])


