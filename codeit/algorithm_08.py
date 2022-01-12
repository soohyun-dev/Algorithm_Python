# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    n=abs(coordinates[1][0]-coordinates[0][0]) + abs(coordinates[1][1]-coordinates[0][1])
    k=n
    s1=coordinates[0]
    s2=coordinates[1]

    for i in range(len(coordinates)-1):
      for j in range(1,len(coordinates)):
        m=abs(coordinates[j][0]-coordinates[i][0]) + abs(coordinates[j][1]-coordinates[i][1])
        if m==0:
          continue
        if m < k:
          k=m
          s1=coordinates[i]
          s2=coordinates[j]
    return [s1, s2]


       
# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))