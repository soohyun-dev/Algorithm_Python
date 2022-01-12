import sys

N=int(input())
l=[]
for i in range(N):
  l.append(sys.stdin.readline().strip())
l_set=set(l)  # set 을 통해 중복된 수들 제거
l_list=list(l_set)  # 리스트 변환
l_list.sort() # 알파벳순 정렬
l_list.sort(key=len)  # 문자 길이 순 정렬

for i in range(len(l_list)):
  print(l_list[i])


  