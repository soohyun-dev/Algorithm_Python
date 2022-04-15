import sys
input=sys.stdin.readline

def check(num, idx):
    global max_num, min_num
    
    if idx==N:
        max_num=max(max_num, num)
        min_num=min(min_num, num)
        return
        
    if C[0]>0:
        C[0]-=1
        check(num+A[idx], idx+1)
        C[0]+=1
    if C[1]>0:
        C[1]-=1
        check(num-A[idx], idx+1)
        C[1]+=1
    if C[2]>0:
        C[2]-=1
        check(num*A[idx], idx+1)
        C[2]+=1
    if C[3]>0:
        C[3]-=1
        check(int(num/A[idx]), idx+1)
        C[3]+=1

N=int(input())
A=list(map(int,input().split()))
C=list(map(int,input().split()))
max_num=0
min_num=0

check(A[0],1)
print(max_num)
print(min_num)