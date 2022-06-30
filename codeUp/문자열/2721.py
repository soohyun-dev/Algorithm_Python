words=[]
for i in range(3):
    words.append(input())
if words[0][-1]==words[1][0] and words[1][-1]==words[2][0] and words[2][-1]==words[0][0]:
    print('good')
else:
    print('bad')