N=input().split('-')
l=[]
for i in range(len(N)):
  p=N[i].split('+')
  if len(p)>1: # 문자안에 + 가 있어서 나누어진 경우
    sum=0
    for j in range(len(p)):
      sum+=int(p[j])
    l.append(sum)
  else:  # + 가 없고 숫자만 있었던 경우
    l.append(int(N[i]))
a=l[0]
for j in range(1,len(l)):
  a-=l[j]
print(a)


    