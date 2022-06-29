N=int(input())
cnt=N//2
for i in range(cnt,-1,-1):
    print(' '*i + '*'*(N-(2*i)))