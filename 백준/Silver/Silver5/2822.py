score=[]
for i in range(1,9):
  score.append([i, int(input())])
score.sort(key=lambda x:-x[1])
sum=0
l=[]
for i in range(5):
  sum+=score[i][1]
  l.append(score[i][0])
print(sum)
l.sort()
for i in range(5):
  print(l[i],end=' ')


  