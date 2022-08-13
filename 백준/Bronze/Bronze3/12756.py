A_a,A_b=map(int,input().split())
B_a,B_b=map(int,input().split())
A=B_b//A_a + (1 if B_b%A_a else 0)
B=A_b//B_a + (1 if A_b%B_a else 0)
if A==B:
    print('DRAW')
elif A>B:
    print("PLAYER B")
elif A<B:
    print("PLAYER A")