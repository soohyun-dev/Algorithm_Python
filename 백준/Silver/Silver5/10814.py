N=int(input())
list=[]
cnt=0
for i in range(N):
  age,name=input().split()
  age=int(age)
  list.append((age, name))

list.sort(key = lambda member: member[0])

for member in list:
  print(member[0], member[1])