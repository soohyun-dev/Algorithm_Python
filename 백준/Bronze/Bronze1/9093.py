for i in range(int(input())):
    l=list(input().split())
    for i in range(len(l)):
        print(l[i][::-1], end=' ')
    print()