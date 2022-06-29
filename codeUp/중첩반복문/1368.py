h,k,d=input().split()
h,k=int(h),int(k)
if d=='R':
    for i in range(h-1,-1,-1):
        print(' '*i+'*'*k)
elif d=='L':
    for i in range(h):
        print(' '*i+'*'*k)