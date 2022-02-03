import sys
from collections import deque
input=sys.stdin.readline

queue=deque([])

for i in range(int(input())):
    key=input().split()

    if key[0]!='push':
        if key[0]=='pop': 
            try:
               print(queue.popleft())
            except:
                print(-1)
        elif key[0]=='size':  
            print(len(queue))
        elif key[0]=='empty':  
            if len(queue)==0:
                print(1)
            else:
                print(0)
        elif key[0]=='front':  
            try:
                print(queue[0])
            except:
                print(-1)
        elif key[0]=='back': 
            try:
                print(queue[-1])
            except:
                print(-1)

    else:  # push X : 정수 X를 큐에 넣는 연산이다.
        queue.append(key[1])

        


