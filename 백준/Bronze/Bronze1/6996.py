import sys 
input=sys.stdin.readline

for i in range(int(input())):
    A,B=map(str,input().split())
    a=sorted(list(A))
    b=sorted(list(B))

    if a==b:
        print("%s & %s are anagrams." %(A,B))
    else:
        print("%s & %s are NOT anagrams." %(A,B))
