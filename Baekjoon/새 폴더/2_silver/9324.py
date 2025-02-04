n = int(input())
# 확인할 메시지의 개수를 받아줍니다
for _ in range(n):
    d = dict()
    result = 'OK'
    massage = input()
    # 메시지를 받고 문장의 개수를 담을 변수와 출력할 결과를 담을 변수를 설정해줍니다
    for i in range(len(massage)):
        j = massage[i]
        d[j] = d.get(j, 0) + 1
        if d[j] == 4 and massage[i] != massage[i - 1]:
            result = 'FAKE'
            break
        elif d[j] == 4:
            d[j] = 0
        # 각 문자의 개수를 담고 4번째 나왔다면 이전 문자와 연속해 유효한지 확인해줍니다
    for i in d:
        if d[i] == 3:
            result = 'FAKE'
            break
    # 문자가 3번 사용되었는데 연속하여 나오지 않은 경우가 있는지 확인해줍니다
    print(result)
    # 결과를 출력해줍니다