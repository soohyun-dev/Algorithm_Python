N=int(input())
l=list(map(int,input().split()))
for i in range(1,N):
  if l[0]%l[i]==0:  # 한번에 나눠질 때
    print('%d/%d' %(l[0]//l[i],1))
  else:
    cnt=l[i]
    while True:  # 최대 공약수 찾기
      if l[0]%cnt==0 and l[i]%cnt==0:  
        print('%d/%d' %(l[0]//cnt,l[i]//cnt))
        break
      cnt-=1



