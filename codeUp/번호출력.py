import random



# 숫자 입력하면 1 부터 그 숫자까지 숫자를 저장한뒤 랜덤으로 돌린다
# 그 중 한 숫자를 지우고 일렬로 출력
N=int(input())
nums=[]
for i in range(1,N+1):
    nums.append(i)
random.shuffle(nums)
del(nums[8])
for i in range(N-1):
    print(nums[i])