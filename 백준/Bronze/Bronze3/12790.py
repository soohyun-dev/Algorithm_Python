import sys
input=sys.stdin.readline

for _ in range(int(input())):
    HP, MP, attack, defend, a, b, c, d=map(int,input().split())
    HP+=a
    MP+=b
    attack+=c
    defend+=d
    if HP<1:
        HP=1
    if MP<1:
        MP=1
    if attack<0:
        attack=0
    print(HP+(MP*5)+(attack*2)+(defend*2))