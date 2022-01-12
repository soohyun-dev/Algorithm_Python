A = int(input())  
B = int(input())
C = int(input())
D = int(input())
P = int(input())
XP = A*P            # X사 요금 (1리터당 요금 * 한달간 수도양)
if(C>P):            # Y사의 상한 보다 적게 사용할경우
  YP=B              # 기본요금
else:               # 상한보다 많이 사용한 경우
  YP=B+((P-C)*D)    # 기본요금 + (초과값*추가요금)
print(min(XP, YP))  # X사요금, Y사요금 중 최솟값 출력

