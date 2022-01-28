numbers=set(range(1,10000))
check_num=set()

for num in numbers:
  for i in str(num):
    num+=int(i)
  check_num.add(num)

self_numbers=sorted(numbers-check_num)

for self_num in self_numbers:
  print(self_num)