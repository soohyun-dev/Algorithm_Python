while True:
    l=list((input()))
    check=[]
    if l[0]=='.' and len(l)==1:
        break
    else:
        for i in range(len(l)):
            if l[i]=='(':
                check.append('(')
            elif l[i]=='[':
                check.append('[')
            elif l[i]==')':
                if '(' in check:
                    if check[-1]=='(':
                        del(check[-1])
                    else:
                        break
                else:
                    check.append('no')
                    break
            elif l[i]==']':
                if '[' in check:
                    if check[-1]=='[':
                        del(check[-1])
                    else:
                        break
                else:
                    check.append('no')
                    break
                
    if len(check)==0:
        print('yes')
    else:
        print('no')
            
            