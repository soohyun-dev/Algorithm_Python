def sol():
    valid=2  # 2부터 제곱수 확인
    while valid**2 <= max:  # max 보다 작은 제곱수들만 확인
        share = min // valid**2  # 제곱수의 배수들을 확인하기 위해 최소 몫을 구함
        while share * (valid**2) <= max:  # max 내의 제곱수의 배수들을 확인
            if (share * (valid**2)) - min <= max and (share * (valid**2)) - min >= 0:
                check[(share * (valid**2) - min)] = 0  # 조건에 해당하는 수들은 0으로 바꿔준다.
            share+=1  # 제곱수의 배수를 높여준다.
        valid+=1
    print(check.count(1))


min, max = map(int, input().split())
check = [1 for i in range(max-min+1)]



sol()



