for i in range(int(input())):
  missNum, S = input().split()
  S=list(S)
  del S[int(missNum)-1]
  for j in range(len(S)):
    print(S[j], end='')
  print()

