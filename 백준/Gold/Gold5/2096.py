import sys
input=sys.stdin.readline

T=int(input())
MAP=[]
for i in range(T):
    MAP.append(list(map(int,input().split())))

MaxDp=[MAP[0][0],MAP[0][1],MAP[0][2]]
MinDp=[MAP[0][0],MAP[0][1],MAP[0][2]]

for i in range(1,T):
    x,y,z=MaxDp[0],MaxDp[1],MaxDp[2]
    MaxDp[0]= max(x,y) + MAP[i][0]
    MaxDp[1]= max(x,y,z) + MAP[i][1]
    MaxDp[2]= max(y,z) + MAP[i][2]
    x,y,z=MinDp[0],MinDp[1],MinDp[2]
    MinDp[0]= min(x,y) + MAP[i][0]
    MinDp[1]= min(x,y,z) + MAP[i][1]
    MinDp[2]= min(y,z) + MAP[i][2]
    
print(max(MaxDp),min(MinDp))