for i in range(int(input())):
  sum=0
  input()
  student=int(input())
  for j in range(student):
    num=int(input())
    sum+=num
  if(sum%student==0):
    print('YES')
  else:
    print('NO')

    