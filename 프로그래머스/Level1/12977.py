def solution(nums):
    result=0
    answer=[]
    answer_check=[]
    visited=[False]*len(nums)
    
    def check(depth):
        if len(answer_check)==3:
            print(answer_check)
            tmp=sum(answer_check)
            if tmp not in answer:
                bool=True
                for i in range(2,tmp//2):
                    if tmp%i==0:
                        bool=False            
                if bool==True:
                    result+=1
            else:
                return
    
        for i in range(len(nums)):
            if not visited:
                visited[i]=True
                answer_check.append(nums[i])
                check(depth+1)
                answer_check.pop()
                visited[i]=False
                
    check(0)

    return result


nums=[1,2,3,4]
print(solution(nums))