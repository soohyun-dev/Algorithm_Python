N=int(input())
l=[]
for i in range(N):
    name,score=input().split()
    l.append([name,int(score)])
    
l.sort(key=lambda x:-x[1])
print(l[2][0])