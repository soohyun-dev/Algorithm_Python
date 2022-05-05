import sys
input=sys.stdin.readline

N,M=map(int,input().split())
DNA=[]
HD=[]

for i in range(N):
    DNA.append(list(input().rstrip()))

for i in range(M):
    T=0
    A=0
    G=0
    C=0
    for j in range(N):
        if DNA[j][i]=='T':
            T+=1
        elif DNA[j][i]=='A':
            A+=1
        elif DNA[j][i]=='G':
            G+=1
        elif DNA[j][i]=='C':
            C+=1
    cnt=max(T,A,G,C)

    tmp=[]
    if cnt==T:
        tmp.append('T')
    if cnt==A:
        tmp.append('A')
    if cnt==G:
        tmp.append('G')
    if cnt==C:
        tmp.append('C')
    
    tmp.sort()
    HD.append(tmp[0])

HD_hap=0
for i in range(N):
    for j in range(M):
        if DNA[i][j]!=HD[j]:
            HD_hap+=1

print(*HD, sep='')
print(HD_hap)
    