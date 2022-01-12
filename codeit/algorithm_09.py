def trapping_rain(buildings):
    # 코드를 작성하세요
    height=buildings[0]
    sum=0
    store=0
    m=max(buildings)
    for i in range(len(buildings)):
      if buildings[i]!=0:
        if height<=buildings[i]:
          height=buildings[i]
          sum+=store
          store=0
          if height==m:
            height==0
        else:
          store+=height-buildings[i]
      else:
        store+=height
    return sum

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))