M=[]
for i in range(10):
  N=int(input())
  M.append(N)
M.sort()
cnt=0
max=0
sum=0
for j in range(10):
  if M.count(M[j]) > cnt:
    cnt = M.count(M[j])
    max=M[j]
  sum+=M[j]
print(int(sum/10))
print(max)


# 다른 답
#a = []

#for i in range(10):
#    a.append(int(input()))

#print(sum(a) // 10)             # 평균
#print(max(a, key=a.count))      # 최빈값
  

