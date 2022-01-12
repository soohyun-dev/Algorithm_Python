K=int(input())
for i in range(1,K+1):
  print('Class %d' %(i))
  score=list(map(int,input().split()))
  max_gap=0
  cnt=score[0]  # 갯수 저장
  score=score[1:]  # 갯수 빼고 값들로만 재정의
  score.sort(reverse=True)  # 값들 내림차순
  for i in range(cnt-1):
    gap=abs(score[i]-score[i+1])  # 값들 차이 구해주기
    if gap>max_gap:  # 가장 큰 차이값 저장
      max_gap=gap
  print('Max %d, Min %d, Largest gap %d' %(max(score),min(score),max_gap))

  