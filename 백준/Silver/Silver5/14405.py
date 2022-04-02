l=['pi','ka','chu']
word=input()
for i in l:
    if i in word:
        word = word.replace(i,'0')
check=True
for j in word:
    if j !='0':
        check=False

if check:
    print('YES')
else:
    print('NO')