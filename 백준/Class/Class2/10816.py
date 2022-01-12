import collections

N=int(input())
have=list(map(int,input().split()))
M=int(input())
N_card=list(map(int,input().split()))
card=collections.Counter(have)

for i in range(M):
  if N_card[i] in card:
    print(card[N_card[i]] , end=' ')
  else:
    print(0, end=' ')

    