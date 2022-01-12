a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c or not(d)) and (not(c) or d))

