N=int(input())
M=N
sum=0

while True:
  a=M//10
  b=M%10
  c=(a+b)%10
  M=(b*10)+c

  sum+=1
  if M==N:
    print(sum)
    break