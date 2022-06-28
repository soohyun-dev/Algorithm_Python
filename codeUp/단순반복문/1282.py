N=int(input())
if N==2:
    t=1
else:
    for i in range(1,N):
        if i*i>N:
            t=i-1
            break
        elif i*i==N:
            t=i
            break
print(N-(t*t), t)
    