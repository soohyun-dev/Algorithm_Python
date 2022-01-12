N=int(input())
day=[]
for i in range(N):
  day.append(list(map(int,input().split())))
cnt=0
pay=[]
day_pay=0
for i in range(N):
  if day[cnt][0]==1: # 1일 만 일하면 될 때
    day_pay+=day[cnt][1]
  else:  # 2일 이상 일해야 할때
    if N>cnt+day[cnt][0]-1:  # 퇴직기간을 넘기는 지 확인
      day_pay+=day[cnt][1]
      cnt+=day[cnt][0]-1
    else:
      cnt+=1
  if cnt>=len(day):
    pay.append(day_pay)
    day_pay=0
    cnt=0
    day.remove(day[0])
  if len(day)<3:
    break
print(max(pay))  
