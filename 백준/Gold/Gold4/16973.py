from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(N)]
H,W,Sr,Sc,Fr,Fc=map(int,input().split())