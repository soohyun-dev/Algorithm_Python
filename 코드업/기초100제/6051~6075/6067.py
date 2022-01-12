num = int(input())

if (num < 0):
  if (num % 2 ==0):
    print("A")
  else:
    print("B")
else: 
  if(num % 2 == 0):
    print("C")
  else:
    print("D")

'''
if (num < 0) and (num % 2 == 0):
  print("A")
if (num < 0) and (num % 2 != 0):
  print("B")
if (num >= 0) and (num % 2 == 0):
  print("C")
if (num >= 0) and (num % 2 != 0):
  print("D")'''