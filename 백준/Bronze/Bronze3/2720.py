for i in range(int(input())):
  num=int(input())
  q=num//25
  d=(num%25)//10
  n=((num%25)%10)//5
  p=((num%25)%10)%5
  print(q, d, n, p)

  