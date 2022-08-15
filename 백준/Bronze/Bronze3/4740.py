while True:
    l=list(input())
    if l[0]=='*' and l[1]=='*' and l[2]=='*' and len(l)==3:
        break
    for i in range(len(l)-1,-1,-1):
        print(l[i],end='')
    print()