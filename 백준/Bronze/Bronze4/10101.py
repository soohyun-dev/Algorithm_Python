a1 = int(input())
a2 = int(input())
a3 = int(input())
if((a1 and a2 and a3)==60):
  print("Equilateral")
elif(a1+a2+a3==180 and (a1 == a2 or a2 == a3)):
  print("Isosceles")
elif(a1+a2+a3==180 and (a1 == a3)):
  print("Isosceles")
elif(a1+a2+a3==180 and (a1!=a2!=a3)):
  print("Scalene")
else:
  print("Error")