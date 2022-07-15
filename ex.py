num=int(input())
l=[]
while num>1:
    num//=2
    for i in range(3):
        l.append(num-i)

print(len(l))