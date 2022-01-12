A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
F=int(input())
M1= min(A,B,C,D)  # 물리, 화학, 생물, 지구과학 중에서 가장 낮은 점수
M2= min(E,F)      # 역사, 지리 중에서 가장 낮은 점수
Total=A+B+C+D+E+F  # 6과목 총점
print(Total-(M1+M2))  # 6과목 총점에서 빼주기

