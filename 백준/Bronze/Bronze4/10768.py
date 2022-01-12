M = int(input())  # 월 입력
D = int(input())  # 일 입력

if(M==1 or (M==2 and D<18)): # 1월이거나 2월인데 18일보다 앞일때
  print("Before")            
elif(M==2 and D==18):  # 2월 18일 일때
  print("Special")
else:                  # 2월 18일 이후
  print("After")

