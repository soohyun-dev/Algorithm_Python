from collections import Counter

case=1

while True:
    first=input()
    second=input()
    if first==second=='END':
        break
    first_dict=Counter(first)
    second_dict=Counter(second)
        
    if first_dict==second_dict:
        print('Case %d: same' %(case))
    else:
        print('Case %d: different' %(case))
        
    case+=1        
        
    