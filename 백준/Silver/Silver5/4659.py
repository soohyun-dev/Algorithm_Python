
while True:
  vowels="aeiou"
  T = input()
  if T == 'end':
    break
  l = list(T)
  check=True

  if (vowels for i in l):  # 모음이 한개이상 있는지 확인
    if len(l)==1:  # 한 글자 일 때
      print("<%s> is acceptable." %(T))
    else:  # 2개 이상의 글자
      v_cnt=0  
      s_cnt=0
      k=l[1]  # 자음이나 모음이 연속되는 체크하기위해 변수 선언
      for i in range(len(l)):
        if k == l[i]:
          if k !='e' and k !='o':
            print("<%s> is not acceptable." %(T))
            check=False
            break # for 문 탈출
        k=l[i]
        if l[i] in vowels:  # 모음이 연속 3번나오는지 체크
          s_cnt=0
          v_cnt+=1
          if v_cnt==3:
            print("<%s> is not acceptable." %(T))
            check=False
            break
        else:  # 자음이 연속 3번나오는지 체크
          v_cnt=0
          s_cnt+=1
          if s_cnt==3:
            print("<%s> is not acceptable." %(T))
            check=False
            break
      if check==True:
        print("<%s> is acceptable." %(T))

  else:  # 모음이 하나라도 없을 경우
    print("<%s> is not acceptable." %(T))
  