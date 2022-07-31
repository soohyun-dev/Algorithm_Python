for _ in range(int(input())):
    word=list(input())
    for i in range(len(word)):
        if word[i].isupper()==True:
            word[i]=word[i].lower()
    print(''.join(word))