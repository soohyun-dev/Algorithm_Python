words=list(input())
for i in range(len(words)):
    if words[i].isalpha():
        cnt=ord(words[i])+13
        if cnt>122:
            cnt-=122
            cnt+=96
        elif cnt>90 and cnt<110:
            cnt-=90
            cnt+=64            
        words[i]=chr(cnt)

print(''.join(words))

