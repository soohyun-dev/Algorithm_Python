word=list(input())
A=''
B=''
for i in range(len(word)):
    A+=chr(ord(word[i])+2)
    B+=chr((ord(word[i])*7)%80+48)
print(A)
print(B)