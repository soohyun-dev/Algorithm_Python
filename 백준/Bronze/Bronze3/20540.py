def Change(word,result):
    if word=='E':
        result.append('I')
    elif word=='I':
        result.append('E')
    elif word=='S':
        result.append('N')
    elif word=='N':
        result.append('S')
    elif word=='T':
        result.append('F')
    elif word=='F':
        result.append('T')
    elif word=='J':
        result.append('P')
    elif word=='P':
        result.append('J')

MBTI=input()
result=[]
for i in range(4):
    Change(MBTI[i],result)
print(''.join(result))
    