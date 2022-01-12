n = int(input())  # 번호를 몇번 부를지 저장한다.
a = input().split() # 어느 번호를 부를지 저장한다.

for i in range(n):  # 부른 번호 수 만큼 배열을 만들기 위해 
  a[i] = int(a[i])  # int 선언후 배열에 넣어준다.

d = []  # d 라는 빈 배열을 선언
for i in range(24):  # d에 24칸을 만들어준 뒤
  d.append(0)        # 각 칸에 0을 넣어준다.

for i in range(n): 
  d[a[i]] += 1  # 입력받은 번호 칸마다 +1 을 해준다.

for i in range(1, 24):
  print(d[i], end=' ')  # 결과 값을 띄어쓰기하여 출력한다.



