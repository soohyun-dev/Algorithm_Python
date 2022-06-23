def solution(answers):
    answer = []
    l=len(answers)
    S=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    check=[0,0,0,0]
    
    # 1번 수포자
    tmp=l//5
    rest=l%5
    A=S[0]*tmp
    A+=S[0][:rest]
    
    # 2번 수포자
    tmp=l//8
    rest=l%8
    B=S[1]*tmp
    B+=S[1][:rest]
    
        
    # 3번 수포자
    tmp=l//10
    rest=l%10
    C=S[2]*tmp
    C+=S[2][:rest]
    
    print(A,B,C)

    # 정답 체크
    for i in range(l):
        if answers[i]==A[i]:
            check[1]+=1
        if answers[i]==B[i]:
            check[2]+=1
        if answers[i]==C[i]:
            check[3]+=1
    M=max(check)
    
    answer=list(filter(lambda x: check[x]==M, range(len(check))))
  
    return answer