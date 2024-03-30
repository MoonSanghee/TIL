while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    # 몇개의 입력이 주어지는지 모르므로 try, except을 이용해 입력이 없으면 멈추어줍니다.

    result = 0
    # 방의 개수를 담을 변수를 만들어줍니다.
    for i in range(n, m + 1):
        number = str(i)
        cnt = set()
        for char in number:
            cnt.add(char)
        if len(number) == len(cnt):
            result += 1
        # 범위안의 정수를 문자열 형태로 바꾸어 순회하며 각 문자를 set형태안에 넣어 중복이 있는지 확인해줍니다.
    
    print(result)
    # result에 담긴 최대 방의 수를 출력해줍니다.