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
            

# [[], [-7], 
# [-3], [-7, -3], 
# [-2], [-7, -2], [-3, -2], [-7, -3, -2], 
# [5], [-7, 5], [-3, 5], [-7, -3, 5], [-2, 5], [-7, -2, 5], [-3, -2, 5], [-7, -3, -2, 5], 
# [8], [-7, 8], [-3, 8], [-7, -3, 8], [-2, 8], [-7, -2, 8], [-3, -2, 8], [-7, -3, -2, 8], 
# [5, 8], [-7, 5, 8], [-3, 5, 8], [-7, -3, 5, 8], [-2, 5, 8], [-7, -2, 5, 8], [-3, -2, 5, 8], [-7, -3, -2, 5, 8]]


