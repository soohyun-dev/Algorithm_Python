a,b,c = map(int, input().split())
t1 = max(a,b,c)
t2 = min(a,b,c)
if (a!= (t1 and t2)):
  print(t2, a, t1)
elif(b!= (t1 and t2)):
  print(t2, b, t1)
elif(c!= (t1 and t2)):
  print(t2, c, t1)
