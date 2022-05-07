import sys
input=sys.stdin.readline

N,M=map(int,input().split())
DNA=[]
HD=[]  # Hamming Distance 합이 가장 작은 DNA

for i in range(N):
    DNA.append(list(input().rstrip()))

for i in range(M):
    T,A,G,C = 0, 0, 0, 0  # 각 열 넘어 갈때마다 초기화

    for j in range(N):  # 각 열에 단어가 몇번나오는지 체크
        if DNA[j][i]=='T':
            T+=1
        elif DNA[j][i]=='A':
            A+=1
        elif DNA[j][i]=='G':
            G+=1
        elif DNA[j][i]=='C':
            C+=1

    cnt=max(T,A,G,C)  # 가장 큰 값 저장
    tmp=[]
    if cnt==T:  # 큰 값에 해당하는 단어 저장
        tmp.append('T')
    if cnt==A:
        tmp.append('A')
    if cnt==G:
        tmp.append('G')
    if cnt==C:
        tmp.append('C')
    
    tmp.sort()  # 정렬로 사전 맨앞 단어만 HD 에 추가. 
    HD.append(tmp[0])

HD_hap=0
for i in range(N):
    for j in range(M):
        if DNA[i][j]!=HD[j]:  # Hamming Distance count
            HD_hap+=1

print(*HD, sep='')
print(HD_hap)


    
