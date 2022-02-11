S=input()
cnt=0
for i in range(int(input())):
    check=0
    l=input()
    l=l*2
    if S in l:
        cnt+=1
print(cnt)