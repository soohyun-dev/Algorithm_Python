for i in range(int(input())):
  c,v=map(int,input().split())
  share=c//v
  rest=c%v
  print("You get %d piece(s) and your dad gets %d piece(s)." %(share, rest))

  