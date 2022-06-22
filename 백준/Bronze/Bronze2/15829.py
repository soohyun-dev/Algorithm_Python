L=int(input())
S=list(input())
sum=0
for i in range(L):
    sum+=(ord(S[i])-96)*(31**i)
print(sum%1234567891)


