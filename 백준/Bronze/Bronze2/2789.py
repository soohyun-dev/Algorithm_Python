Delete = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
voca=input()
for i in range(len(voca)):
  if voca[i] not in Delete:
    print(voca[i], end='')


