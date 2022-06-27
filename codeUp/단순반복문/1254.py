x,y=input().split()
start=ord(x)
end=ord(y)
for i in range(start,end+1):
    print(chr(i), end=' ')
print('a')