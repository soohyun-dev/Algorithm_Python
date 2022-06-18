def solution(id_list, report, k):
    answer = []
    report=set(report)
    report=list(report)
    report.sort(key=lambda x:x.split(' ')[1])
    cnt=0
    member=[]
    check=report[0].split(' ')[1]
    mail={}
    for i in id_list:  
        mail[i]=0
    
    for i in range(len(report)):
        x,y=report[i].split(' ')
        if y==check:
            member.append(x)
            cnt+=1        
        if (y!=check) or (i==(len(report)-1)):
            if cnt>=k:
                for j in member:
                    tmp=mail[j]
                    mail[j]=tmp+1
            member=[]
            member.append(x)
            cnt=1
            check=y       
   
    for k in id_list:
        answer.append(mail[k])
    
    return answer
