import sys
input=sys.stdin.readline

for _ in range(int(input())):
    score=[0,0]
    for i in range(9):
        a,b=map(int,input().split())
        score[0]+=a
        score[1]+=b
    if score[0]>score[1]:
        print("Yonsei")
    elif score[0]==score[1]:
        print("Draw")
    elif score[0]<score[1]:
        print("Korea")
