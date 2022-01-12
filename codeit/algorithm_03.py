# 이진 탐색 알고리즘

def binary_search(element, some_list):
  sum=0
  while True:
    f_index=len(some_list)//2
    if element==some_list[f_index]:
      sum+=f_index
      return sum
    elif element>some_list[f_index]:
      sum+=f_index
      some_list=some_list[f_index:len(some_list)]
    elif element<some_list[f_index]:
      some_list=some_list[0:f_index]
      if f_index==0:
        return None

     
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))