a1, a2, a3, A1, A2, A3 = map(int, input().split())
b1, b2, b3, B1, B2, B3 = map(int, input().split())
c1, c2, c3, C1, C2, C3 = map(int, input().split())

at3 = A3-a3
if (at3<0):
  A2=A2-1
  at3=60+at3
at2 = A2-a2
if(at2<0):
  A1=A1-1
  at2=60+at2
at1 = A1-a1
print(at1, at2, at3)

bt3 = B3-b3
if (bt3<0):
  B2=B2-1
  bt3=60+bt3
bt2 = B2-b2
if(bt2<0):
  B1=B1-1
  bt2=60+bt2
bt1 = B1-b1
print(bt1, bt2, bt3)

ct3 = C3-c3
if (ct3<0):
  C2=C2-1
  ct3=60+ct3
ct2 = C2-c2
if(ct2<0):
  C1=C1-1
  ct2=60+ct2
ct1 = C1-c1
print(ct1, ct2, ct3)