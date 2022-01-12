a,b,c,d,e,f=map(int,input().split())

for i in range(-999,1000):
  for j in range(-999, 1000):
    if (a*i)+(b*j)==c and (d*i)+(e*j)==f:
      print(i,j)


'''
a,b,c,d,e,f=map(int,input().split())
mul1=b
mul2=e
# y 의 계수 맞추기
a=mul2*a
b=mul2*b
c=mul2*c
d=mul1*d
e=mul1*e
f=mul1*f
# y 계수의 부호가 서로 같을때
if b==e:
  A=a-d
  C=c-f
  x=C//A # x값

# y 계수의 부호가 서로 다를때
else:
  A=a+d
  C=c+f
  x=C//A  # x값
# x 대입후 '=' 반대쪽으로 넘겨서 연산해 y 값 구하기
c=-(a*x)+c
y=c//b

print(x, y)

'''
