import sys 
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
binary=[0]

for num in A:
    if binary[-1] < num:
        binary.append(num)
    else:
        start, end = 0, len(binary)
        
        while start < end: 
            divide=(start+end)//2

            if binary[divide] < num:
                start = divide+1
            else:
                end = divide

        binary[end]=num
        
print(len(binary[1:]))


