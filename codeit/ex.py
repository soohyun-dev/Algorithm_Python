vowels = {
  'a' ,'e', 'i', 'o', 'u'
}


T = input()

l = list(T)
check=True

if all(l for num in vowels): 
  print(True)

