R,C,N = map(int,input().split())

if(C%N!=0):  # 열의 범위에서 최대한 적게 CCTV 배치
  a=(C//N)+1
else:
  a=(C//N)

if(R%N!=0):  # 행의 범위에서 최대한 적게 CCTV 배치
  b=(R//N)+1
else:
  b=(R//N)

print(a*b)  # 두 값 곱해서 전체 CCTV 수 출력

