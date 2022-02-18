from collections import deque

def rotate_right(num,direction): 
    if num>4:
        return
    
    if check[num-1]==False:
        Gear[num].rotate(direction)
        rotate_right(num+1,-direction)

def rotate_left(num,direction): 
    if num<1:
        return

    if check[num]==False:
        Gear[num].rotate(direction)
        rotate_left(num-1,-direction)


Gear=[0]
for i in range(4):
    Gear.append(deque(list(map(int,list(input())))))

for _ in range(int(input())):
    num, direction = map(int,input().split())
    check=[True, Gear[1][2]==Gear[2][6], Gear[2][2]==Gear[3][6], Gear[3][2]==Gear[4][6], True]

    Gear[num].rotate(direction)
    rotate_right(num+1, -direction)
    rotate_left(num-1, -direction)
    
score=0

for i in range(4):
    if Gear[i+1][0]==1:
        score+=2**i

print(score)

