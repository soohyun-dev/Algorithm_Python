yeondoo=input()
N=int(input())
max,max_i=0,0
name=sorted([input() for i in range(N)])
for i in range(N):
  L=yeondoo.count("L")+name[i].count("L")
  O=yeondoo.count("O")+name[i].count("O")
  V=yeondoo.count("V")+name[i].count("V")
  E=yeondoo.count("E")+name[i].count("E")
  result=((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
  if max<result:
    max_i=i
    max=result
print(name[max_i])



