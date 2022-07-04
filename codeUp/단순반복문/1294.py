code=list(input().split())
result=[]
for i in range(len(code)):
    word=''
    for j in range(len(code[i])):
        if code[i][j]=='x' or code[i][j]=='y' or code[i][j]=='z':
            tmp=ord(code[i][j])
            word+=chr(tmp-23)
        else:
            tmp=ord(code[i][j])
            word+=chr(tmp+3)
    
    result.append(word)
    
print(*result)