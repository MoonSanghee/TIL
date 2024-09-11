while True:
    n = int(input())
    # 페이지의 제한범위를 받아줍니다.
    if n == 0:
        break
    # 범위가 0이 주어지면 작동을 멈추어줍니다.
    else:
        pages = list(input().split(','))
        # 콤마를 기준으로 나누어줍니다.
        result = set()
        for page in pages:
            if '-' not in page:
                start, end = int(page), int(page)
            else:
                start, end = map(int, page.split('-'))
            if start > end:
                continue
            else:
                for i in range(start, end + 1):
                    if i <= n:
                        result.add(i)
            # 하이푼이 없으면 시작과 끝이 한 페이지이므로 같은 수로 설정해줍니다.
            # 시작이 끝 페이지보다 뒤 페이지면 확인할 필요가없습니다.
            # 주어진 범위 안이면 세트형 result 안에 넣어줍니다.
        print(len(result))
        # result의 길이를 출력해줍니다.