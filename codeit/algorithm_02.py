# 선형 탐색 알고리즘

def linear_search(element, some_list):
    sum=0
    for i in range(len(some_list)):
        if some_list[i]==element:
            return i

    
print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))