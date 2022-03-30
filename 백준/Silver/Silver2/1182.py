N,S=map(int,input().split())
nums=list(map(int,input().split()))
answer_check=[[]]
answer=[]
cnt=0

for num in nums:
    l=len(answer_check)
    for i in range(l):
        answer_check.append(answer_check[i]+[num])
        if sum(answer_check[i]+[num])==S:
            cnt+=1
print(cnt)
            

