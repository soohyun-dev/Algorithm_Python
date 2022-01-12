X=int(input())
a=1  # 분자
b=1  # 분모
max=1
change='up' # 방향
if X!=1:
  for i in range(1,X):
    if change=='down':
      if max==a:
        a+=1
        b=1
        max+=1
        change='up'
      else:
        b-=1
        a+=1
    elif change=='up':
      if max==b:
        b+=1
        max+=1
        change='down'
      else:
        a-=1
        b+=1
print('%d/%d'%(a,b))

