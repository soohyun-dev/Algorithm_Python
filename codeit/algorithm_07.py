def max_product(left_cards, right_cards):
  l=[]
  for i in range(len(left_cards)):
    for j in range(len(right_cards)):
      l.append(left_cards[i]*right_cards[j])
  return(max(l))
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))