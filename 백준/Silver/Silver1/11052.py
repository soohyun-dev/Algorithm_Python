import sys
input = sys.stdin.readline

N=int(input())
card=[0]+list(map(int,input().split()))  # index 맞춰주기
check=[0]*(N+1)

for num in range(1,N+1):
  for cnt in range(num+1):
    check[num]=max(check[num],check[num-cnt]+card[cnt])  # 최댓값을 부여

print(max(check))
      

  