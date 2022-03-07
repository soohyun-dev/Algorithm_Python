import sys
input=sys.stdin.readline

def gcd(up,down):
    if up%down==0:
        return down
    else:
        return gcd(down,up%down)

A,B=map(int,input().split())
C,D=map(int,input().split())

A=A*D+B*C
B=B*D
tmp=gcd(A,B)  # 최대공약수 구하기
print(A//tmp, B//tmp)



