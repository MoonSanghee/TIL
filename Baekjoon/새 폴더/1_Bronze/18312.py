n, k = map(int, input().split())
cnt = 0
k = str(k)
# 두 정수를 받고 수의 개수를 담을 변수를 만들고 k를 문자열 형태로 바꾸어줍니다
for h in range(n + 1):
    if h < 10:
        h = '0' + str(h)
    else:
        h = str(h)
    # 시간 단위가 한자리수라면 앞에 0을 붙여 2자리를 맞추어줍니다
    for m in range(60):
        if m < 10:
            m = '0' + str(m)
        else:
            m = str(m)
        # 분단위가 한자리수라면 앞에 0을 붙여 2자리를 맞추어줍니다
        for s in range(60):
            if s < 10:
                s = '0' + str(s)
            else:
                s = str(s)
            # 초단위가 한 자리수라면 앞에 0을 붙여 2자리를 맞추어줍니다
            time = h + m + s
            if k in time:
                cnt += 1
            # 시간을 문자열형태로 붙여 k들어있는지 확인해줍니다

print(cnt)
# 결과를 출력해줍니다