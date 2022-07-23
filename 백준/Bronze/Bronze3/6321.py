N=int(input())
for i in range(N):
    word=list(input())
    for j in range(len(word)):
        tmp=ord(word[j])
        if tmp==90:
            tmp=64
        word[j]=chr(tmp+1)
    print('String #%d' %(i+1))
    for k in range(len(word)):
        print(word[k],end='')
        if k==len(word)-1:
            print()
    if i!=N-1:
        print()
        