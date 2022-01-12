import sys

N,M=map(int,input().split())
dict={}

for i in range(1,N+1):
  pokemon=sys.stdin.readline().rstrip()
  dict[i]=pokemon
  dict[pokemon]=i

for j in range(M):
  answer=sys.stdin.readline().rstrip()
  if answer.isalpha()==False:
    print(dict[int(answer)])
  else:
    print(dict[answer])


