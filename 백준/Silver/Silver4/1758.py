import sys
input=sys.stdin.readline

N=int(input())
line=[]
for i in range(N):
    line.append(int(input()))  
line.sort(reverse=True)

sum=0
for i in range(N):
    if line[i]-i>0:
        sum+=(line[i]-i)
print(sum)