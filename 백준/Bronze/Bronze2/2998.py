Octal = {
  '000' : 0 ,
  '001' : 1 ,
  '010' : 2 ,
  '011' : 3 ,
  '100' : 4 ,
  '101' : 5 ,
  '110' : 6 ,
  '111' : 7
}
N=input()
while len(N)%3!=0:
  N=str(N).zfill(len(N)+1)
for i in range(0,len(N),3):
  a=N[i:i+3]
  print(Octal[a], end='')

