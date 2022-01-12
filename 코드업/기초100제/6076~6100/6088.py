a, d, num = map(int, input().split())  # 3 정수를 받는다. 1. 초기값, 2. 공차 3. 항 개수
cnt=1 # 카운트를 세줄 변수를 선언한다.
while (cnt<num):
  a+=d  # 항에 공차를 더해준다.
  cnt+=1  # 항에 공차를 더할때마다 카운트가 올라간다.
print(a) # 마지막 값을 출력해준다.

'''
print(a+(d*(num-1))
'''