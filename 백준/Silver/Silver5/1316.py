n=int(input())
sum=0
for i in range(n):
  a=list(input())
  l=[]  # 문자의 연속이 끝나는 지점을 파악하기 위해 따로 저장.
  real=[] # 연속이 끝난 문자들 저장, real 에 저장된 문자는 더이상 나오면 안된다.
  b=0
  for j in range(len(a)):
    if a[j] not in l:
      l.append(a[j])
    if a[j-1]!=a[j] and a[j-1] in l: # 문자의 연속이 끝나는 지점
      real.append(a[j-1])
    if a[j] in real:  # 앞에 나온 문자가 또 나오는 경우
      b=1
      break
  if b==0:  # 그룹단어인지 확인용
    sum+=1
print(sum)



