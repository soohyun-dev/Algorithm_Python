import math
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    arr=list(map(int,input().split()))
    result=0
    for i in range(1,arr[0]+1):
        for j in range(i+1,arr[0]+1):
            result+=math.gcd(arr[i],arr[j])
    print(result)