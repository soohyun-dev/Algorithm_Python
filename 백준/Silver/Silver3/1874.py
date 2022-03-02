import sys
input=sys.stdin.readline

n=int(input())
stack=[]
order=[]
check=[True]*(n+1)
for i in range(n):
    num=int(input())
    if check[num]==False:
        order=['NO']
        break
    if i==0:
        tmp=num
        for j in range(1,num+1): 
            stack.append(j)
            order.append('+')
    elif len(stack)==0:
        for i in range(tmp+1,num+1):
            stack.append(i)
            order.append('+')
        tmp=num     
    elif num>stack[-1]:
        while num!=stack[-1]:
            stack.append(tmp+1)
            order.append('+')
            tmp=tmp+1
            
    if num==stack[-1]:
        a=stack.pop()
        order.append('-')
        check[a]=False
        
    else:
        while num!=stack[-1]:
            a=stack.pop()
            order.append('-')
            check[a]=False

for i in order:
    print(i)