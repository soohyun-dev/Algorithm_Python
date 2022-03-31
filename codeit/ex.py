
while True:
    a,b = map(int,input().split())
    print(a//b, a%b)
    if a==0 and b==0:
        break