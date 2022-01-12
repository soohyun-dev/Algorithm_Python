N,L=input().split()
cnt=0
label_Max=0

while cnt!=int(N):
  label_Max+=1
  if L in str(label_Max):
    continue
  cnt+=1

print(label_Max)
    

