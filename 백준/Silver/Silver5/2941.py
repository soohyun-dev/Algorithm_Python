croatia = {
  'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='
}

word=str(input())
cnt=0
total=0

while cnt<len(word):
  if  (cnt+1<len(word)) and (word[cnt]+word[cnt+1] in croatia)  :
    cnt+=2
    total+=1
  elif (cnt+2<len(word)) and (word[cnt]+word[cnt+1]+word[cnt+2] in croatia):
      cnt+=3
      total+=1
  else:
    cnt+=1
    total+=1

print(total)


