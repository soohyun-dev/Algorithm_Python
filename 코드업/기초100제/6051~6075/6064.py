x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
a = (x if (x<=y) else y) if (y <= z) else (x if (x <= z) else z)
print(a)

