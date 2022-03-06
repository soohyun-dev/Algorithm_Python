S=list(map(str,input()))
i=0
while i< len(S):
    if '<' == S[i]:
        i+=1
        while '>'!=S[i]:
            i+=1
        i+=1
    elif S[i]==' ':
        i+=1
    else:
        start=i
        while i < len(S) and S[i].isalnum():
            i+=1
        word=S[start:i]
        word.reverse()
        S[start:i] = word


print("".join(S))