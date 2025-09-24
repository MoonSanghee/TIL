while True:
    try:
        n = input()
        s = set(list(n))
        num = 0
        # 수를 받고 각 한자리 숫자를 담을 세트형 변수와 배수를 담을 변수를 만들어줍니다
        k = 0
        # 결과를 담을 변수를 설정해줍니다
        while len(s) < 10:
            num += int(n)
            check = set(list(str(num)))
            s = s.union(check)
            k += 1
        # 0부터 9까지의 모든 수가 나올때까지 주어진 수를 더하여 없는 수가 충분히 추가되었는지 확인해줍니다
        print(k)
        # 모든 수가 등장하는 가장 작은 k를 출력해줍니다
    except:
        break