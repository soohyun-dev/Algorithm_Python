l=list(input())
for i in range(len(l)):
    if l[i].isdigit()==False:
        l[i]=l[i].swapcase()

print(''.join(l))