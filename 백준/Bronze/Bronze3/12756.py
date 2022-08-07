A_a,A_b=map(int,input().split())
B_a,B_b=map(int,input().split())
A=B_b//A_a + (B_b%A_a)
B=A_b//B_a + (A_b%B_a)
if A==B:
    print('DRAW')
elif A>B:
    print("PLAYER B")
elif A<B:
    print("PLAYER A")