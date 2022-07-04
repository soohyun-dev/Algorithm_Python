from socket import CAN_BCM_RX_CHECK_DLC


word=list(input())
cnt=0
l=[]
for i in range(len(word)):
    if word[i]=='c' or word[i]=='C':
        cnt+=1
        if i==len(word)-1:
            l.append(cnt)
    else:
        if cnt!=0:
            l.append(cnt)
        cnt=0
    
c=0
cc=0
        
for i in range(len(l)):
    if l[i]==1:
        c+=1
    else:
        c+=l[i]
        cc+=(l[i]-1)
        
print(c)
print(cc)


