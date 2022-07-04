words=list(input())
cnt=0
i=0
check=['U','C','P','C']
while cnt<len(words) and i<4:
    if words[cnt]==check[i]:
        i+=1
    cnt+=1

if i==4:
    print('I love UCPC')
else:
    print('I hate UCPC')
    
    
    