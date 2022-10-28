T=int(input())
for i in range(T):
    S=list(input())
    answer=0
    dict={}
    for i in range(65,91):
        dict[chr(i)]=i
    for j in S:
        dict[j]=0
    for k in range(65,91):
        if (dict[chr(k)]!=0):
            answer+=dict[chr(k)]
    print(answer)