octopus = {
  '-' : 0,
  '\\' : 1,
  '(' : 2,
  '@' : 3,
  '?' : 4,
  '>' : 5,
  '&' : 6,
  '%' : 7,
  '/': -1
}
while(True):
  s=input()
  if s[0]=="#":
    break
  sum=0
  for i in range(len(s)):
    sum+=octopus[s[i]]*8**(len(s) - i -1)
  print(sum)