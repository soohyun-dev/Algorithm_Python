N=int(input())
a=str(N)
start=N-9*len(a)
if start<0:  # 음수 나오면 최소 1까지 올려주기
  start=1
end=0
for i in range(start,N+1):
  n=str(i)
  sum=0
  for j in range(len(n)):    
    sum+=int(n[j])
  if i+sum==N:
    end=i
    break   # 최솟값 구하는 문제이므로 처음 나온 수에서 break
            # 만약 최댓값이라면 break 안써주고 계속 돌려주면됨
if end==0:
  print(0)
else:
  print(end)


