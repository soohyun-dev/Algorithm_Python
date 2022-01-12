while True:
  n=int(input())
  if n==0:
    break
  l=[]
  for i in range(n):
    word=input()
    l.append(word)
  l.sort(key=lambda word: word.lower())
  print(l[0])