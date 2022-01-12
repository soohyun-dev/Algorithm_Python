for i in range(int(input())):
  size=int(input())
  for i in range(size):
    if(i==0):
      print('#'*size)
    elif(i!=0 and i!=size-1):
      print('#'+'J'*(size-2)+'#')
    else:
      print('#'*size)
  print()


