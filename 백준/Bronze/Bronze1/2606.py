computer=int(input())

T=int(input())
link=[]
for i in range(T):
  link.append(list(map(int,input().split())))
link.sort()  # for 문 처음 1부터 받기 위함

virus=[1]  # 바이러스 걸린 컴퓨터들 저장

for i in range(len(link)):
  for j in range(2):
    if link[i][j] in virus:
      if j==0:
        virus.append(link[i][j+1])
        break
      else:
        virus.append(link[i][j-1])

virus=set(virus)  # 중복된 컴퓨터 번호들 정리
print(len(virus)-1)  # 1 은 빼고 출력



