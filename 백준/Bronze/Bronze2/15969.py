N=int(input())
l=list(map(int,input().split()))
l.sort()
print(l[N-1]-l[0])


