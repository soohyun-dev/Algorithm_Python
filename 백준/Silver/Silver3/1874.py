import sys
input=sys.stdin.readline

n=int(input())
stack=[]
order=[]
check=[True]*(n+1)

for i in range(n):
    num=int(input())
    if check[num]==False:  # 이미 pop 시킨 숫자가 나오면, 불가능한 경우이다.
        order=['NO']
        break

    if i==0:  # 첫번째로 받은 숫자는 크기만큼 스택에 쌓아준다.
        tmp=num
        for j in range(1,num+1): 
            stack.append(j)
            order.append('+')

    elif len(stack)==0:  # 만약 pop을 시킨 후에 안이 비게 될 경우를 방지 
        for i in range(tmp+1,num+1):
            stack.append(i)
            order.append('+')
        tmp=num     
    elif num>stack[-1]:  #  입력 숫자가 스택 끝 숫자보다 클경우 쌓아주기 
        while num!=stack[-1]:
            stack.append(tmp+1)
            order.append('+')
            tmp=tmp+1
            
    if num==stack[-1]:  # 스택 끝값이 찾는 값이면 pop 시키고, pop 되었다고 표시
        a=stack.pop()
        order.append('-')
        check[a]=False
        
    else:  # 출력시킬값이 끝값이 아니면 값을 찾을때까지 pop
        while num!=stack[-1]:
            a=stack.pop()
            order.append('-')
            check[a]=False

for i in order:
    print(i)

