l=list(input())
check=[0]*26
for i in range(len(l)):
    if l[i].isalpha()==True:
        check[ord(l[i])-97]+=1

for i in range(26):
    print('%s:%d' %(chr(i+97), check[i]))