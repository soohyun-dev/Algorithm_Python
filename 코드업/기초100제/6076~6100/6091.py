h1, h2, h3 = map(int, input().split())
day = 1
while(day%h1 != 0 or day%h2 != 0 or day%h3 != 0):  # 3명의 사람이 모두 해당되는 날을 찾는다.
  day+=1
print(day)


