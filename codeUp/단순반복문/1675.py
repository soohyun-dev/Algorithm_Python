code=list(input().split())
result=[]
for i in range(len(code)):
    word=''
    for j in range(len(code[i])):
        if code[i][j]=='a' or code[i][j]=='b' or code[i][j]=='c':
            tmp=ord(code[i][j])
            word+=chr(tmp+23)
        else:
            tmp=ord(code[i][j])
            word+=chr(tmp-3)
    
    result.append(word)
    
print(*result)