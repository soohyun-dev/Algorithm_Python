num=int(input())

for i in range(2,num):
    L=num//i
    L=L//i
    if L==1:
        print(i)
        break