for i in range(int(input())):
  l = sorted(map(int,input().split()))
  if l[0]+l[1] <= l[2]:
    print('Case #%d: invalid!' %(i+1))
  else:
    if(l[0]==l[1]==l[2]):
      print('Case #%d: equilateral' %(i+1))
    elif(l[0]==l[1] or l[1]==l[2] or l[2]==l[0]):
      print('Case #%d: isosceles' %(i+1))
    elif(l[0]!=l[1]!=l[2]):
      print('Case #%d: scalene' %(i+1))

      