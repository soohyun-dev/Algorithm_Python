place=[]
for i in range(10):
    place.append(list(map(int,input().split())))
    
x,y=2,2
place[1][1]=9

while x<10 and y<10:
    if place[x-1][y]!=1:
        y+=1
        place[x-1][y-1]=9
    elif place[x][y-1]!=1:
        x+=1
        place[x-1][y-1]=9
    elif place[x][y-1]==1 and place[x-1][y]==1:
        break
    if place[x][y-1]==2 or place[x-1][y]==2:
        if place[x][y-1]==2:
            place[x][y-1]=9
        elif place[x-1][y]==2:
            place[x-1][y]=9
        break

for i in range(10):
    print(*place[i])