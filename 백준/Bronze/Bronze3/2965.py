x=0
sum=0
A,B,C=map(int,input().split())

while True:
  if B-A==1 and C-B==1:
    print(sum)
    break
  elif B-A>=C-B:
    C=B-1
    x=C
    C=B
    B=x
    sum+=1
  elif B-A<C-B:
    A=B+1
    x=A
    A=B
    B=x
    sum+=1